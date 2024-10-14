# ETJump Mapscripting

ETJump adds new scripting actions, events and entities for mapscripting. Below is a list of new scripting actions, as well as any additions to existing ones.

---

## create

```
create
{
    <classname> <value>
    [key1] <value>
    [key2] <value>
    ...
}
```

```{note}
The documentation of this script action is possibly lacking and inaccurate.
```

Allows limited spawning of entities in a map. `create` must be called as a first thing inside `game_manager` -> `spawn` script action. If a map lacks `script_multiplayer` or the `game_manager` script block, it should be called at another entitys `spawn` block. If a map does not include a `script_multiplayer` entity and there are no entities with a `scriptname` set, ETJump automatically spawns an `etjump_game_manager` entity, which provides an entry point to the mapscript via `etjump_manager` scriptblock.

Each entity must be given `classname` and `origin` keys, and additionally for `trigger_multiple_ext`, `trigger_starttimer_ext`, `trigger_checkpoint_ext`, `trigger_stoptimer_ext` and `func_fakebrush`, the brushmodel `mins` and `maxs` (and `contents` in case of `func_fakebrush`). Spawning of point entities generally works as if you would make them in map editor (just remember to set `origin` key manually), but spawning of brush entities is severly limited. Such limits include, but are not necessarily limited to:

* Only the following brush entities can be spawned without using an existing brush model from the map. Any other brush entity will spawn, but lack any volume and act as if they are point entities, even if `mins/maxs` are set.
    * `trigger_multiple_ext`
    * `trigger_starttimer_ext`
    * `trigger_checkpoint_ext`
    * `trigger_stoptimer_ext`
    * `func_fakebrush`
* Spawning of visible brushwork only works by reusing the geometry of an existing brush entity in the map - it's not possible to create your own, visible brushmodel with specific textures.
* You cannot set surfaceparms, only contentparms can be modified with `contents <integer>` key, see [surfaceflags.h](https://github.com/etjump/etjump/blob/94fc83ead2192755a858a0ce761d705b4b145d4e/src/game/surfaceflags.h#L6-L37).
    * Some contentparms are compile-time only, such as `CONTENTS_LIGHTGRID` and `CONTENTS_AREAPORTAL`, and cannot be used.

### Reusing brushmodels

To reuse geometry from an existing brush entity in the map, use the `model "*N"` key, where `N` corresponds to the number of the brushmodel you want to use. To find out this number, open the BSP file of the map in any text editor, find the entity from which you want to reuse geometry from, and check the model number (e.g. `"model" "*12"`). This is the only way to create visible brush entities, and the only create a new brush entity with volume, apart from the entities mentioned above.

Example from `oasis.bsp`:

```
{
"model" "*12" // this is the model key we want
"scriptname" "water_pump_1"
"targetname" "water_pump_1"
"spawnflags" "8"
"track" "wp1"
"classname" "func_constructible"
}
```

```{caution}
If the brushmodel you are reusing is visible at the same time as the original brushmodel, either might become invisible.
```

```{caution}
When setting the `origin` key, the value is relative to the brushmodel you are reusing, meaning you are "moving" the brushmodel from its original postion rather than setting an absolute position.
```

```{hint}
Reusing another brushmodel does not remove the original, but rather duplicates it. This means that it's possible to reuse same brushmodel multiple times for different entities.
```

### Examples

Creating a new spawnpoint with a commmand map icon.

```
game_manager
{
    spawn
    {
        create
        {
            classname "team_WOLF_objective"
            description "Extra Spawn"
            origin "-16 512 64"
            spawnflags "1" // DEFAULT_AXIS
        }
        create
        {
            classname "team_CTF_redspawn"
            origin "-16 560 64"
            spawnflags "3" // INVULNERABLE | STARTACTIVE
        }
    }
}
```

Creating a trigger which activates a print, using [`etjump_game_manager`](mapping_entities.md/#etjump_game_manager).

```
etjump_manager
{
    spawn
    {
        create
        {
            classname "trigger_multiple_ext"
            origin "224 -96 40"
            mins "-32 -32 -32"
            maxs "32 32 32"
            target "print_entity"
        }
        create
        {
            classname "target_print"
            message "Hello!"
            origin "192 0 64"
            targetname "print_entity"
        }
    }
}
```

Creating a `func_invisible_user` which activates a print, along with visible brushwork to indicate it's location.

```
game_manager
{
    spawn
    {
        create
        {
            classname "func_invisible_user"
            cursorhint "HINT_ACTIVATE"
            origin "0 -540 0"
            model "*1" // a random func_explosive in the map
            target "print"
        }
        create
        {
            classname "script_mover"
            scriptname "invis_bmodel"
            origin "0 -540 0"
            model "*1" // using same brushmodel as above to match size
        }
        create
        {
            classname "target_printname"
            message "Hello!"
            origin "192 0 64"
            targetname "print"
        }
    }
}
```

Supply ETPro mapscript, using `func_fakebrush` to fix satchel exploit at crane controls.

```
// mortis - satchel exploit fix part one
create
{
    scriptName "bugfix2"
    classname "func_fakebrush"
    origin "721 -1663 384"
    contents 1  // CONTENTS_SOLID
    mins "-66 -4 -64"
    maxs "66 8 64"
}

// mortis - satchel exploit fix part two
create
{
    scriptName "bugfix3"
    classname "func_fakebrush"
    origin "787 -1633 384"
    contents 1  // CONTENTS_SOLID
    mins "-8 -32 -64"
    maxs "8 72 64"
}
```

---

## cvar set/inc/random

`cvar <cvarname> set/inc/random <value>`

These mapscript actions have been removed from ETJump as they can be used for malicious purposes, e.g. changing `rconPassword` on server.

---

## damageplayer

`damageplayer <damage>`

Damages player by given amount.

```{note}
If the player has `etj_nofatigue 1`, the damage is halved due to the constant adernaline the cvar gives to the player.
```

```{caution}
This script action **must** be called via an entity that passes activator data!
```

---

## etjump_manager

Acts as an entry point for mapscript. If a map contains no `script_multiplayer` or any entities with a `scriptname` set, you can use this script block to access mapscripting in a map, e.g. for spawning entities using [create]. This is only present in maps which do not provide `script_multiplayer` or entities with a `scriptname` set.

---

## func_fakebrush

`func_fakebrush` is a special brush entity that can be spawned via mapscripts. Historically it is used in ETPro to fix exploits in maps. It can act as a clip brush for example to prevent players from jumping out of the map, if the mapper has failed to clip the map properly. To spawn a `func_fakebrush`, you must set the following keys: `origin`, `mins`, `maxs` and `contents`.

```{hint}
When `g_scriptDebug` is set to **1**, this entitys bounding box will be drawn in red.
```

---

## killplayer

`killplayer`

Kills the player as if they used `/kill` command.

```{caution}
This script action **must** be called via an entity that passes activator data!
```

---

## setplayerautospawn

`setplayerautospawn <objective description>`

Sets the activating players auto spawnpoint to specified spawnpoint. `objective description` is the `description` key of `team_WOLF_objective` (visible next to the clickable flag on command map). Spawnpoint name must be inside quotes if it contains spaces (eg. `setplayerautospawn "Forward Bunker"`).

```{caution}
This script action **must** be called via an entity that passes activator data!
```

---

## setplayerspawn

`setplayerspawn <objective description>`

Sets the activating players current spawnpoint to specified spawnpoint. `objective description` is the `description` key of `team_WOLF_objective` (visible next to the clickable flag on command map). Spawnpoint name must be inside quotes if it contains spaces (eg. `setplayerspawn "Forward Bunker"`).

```{caution}
This script action **must** be called via an entity that passes activator data!
```

---

## tracker

`tracker [index] <command> <value>`

Manipulates or checks activators tracker values. If index is not set, defaults to index **1**.

| Command               | Description                                                                        |
| --------------------- | ---------------------------------------------------------------------------------- |
| set                   | Sets activators tracker value                                                      |
| inc                   | Increases tracker value                                                            |
| abort_if_less_than    | Abort script execution is activators tracker value is less than specified          |
| abort_if_greater_than | Abort script execution is activators tracker value is greater than specified       |
| abort_if_not_equal    | Abort script execution is activators tracker value not equal to specified value    |
| abort_if_equal        | Abort script execution is activators tracker value is equal to specified value     |
| bitset                | Sets activators tracker bit                                                        |
| bitreset              | Resets activator tracker bit                                                       |
| abort_if_bitset       | Abort script execution is activators tracker value has specified bit set           |
| abort_if_not_bitset   | Abort script execution is activators tracker value does not have specified bit set |

```{caution}
This script action **must** be called via an entity that passes activator data!
```

```{seealso}
[target_tracker and trigger_tracker](mapping_entities.md/#target_tracker-and-trigger_tracker)
```

---

## trigger_checkpoint_ext

Used for spawning a `trigger_checkpoint` entity. You must set `mins`, `maxs` and `origin` keys for this manually. Supports same entity keys and spawnflags as regular `target/trigger_checkpoint`.

```{hint}
When `g_scriptDebug` is set to **1**, this entitys bounding box will be drawn in magenta.
```

---

## trigger_multiple activate event

`activate allies/axis`

`trigger_multiple` activation passes `team` parameter to script, allowing you to define different script actions to trigger depending on the activators team.

```
mytrigger
{
    activate axis
    {
        wm_announce "Activated by Axis player"
    }
    activate allies
    {
        wm_announce "Activated by Allied player"
    }
}
```

---

## trigger_multiple_ext

Used for spawning a `trigger_multiple` entity. You must set `mins`, `maxs` and `origin` keys for this manually. Supports same entity keys and spawnflags as regular `trigger_multiple`.

```{hint}
When `g_scriptDebug` is set to **1**, this entitys bounding box will be drawn in green.
```

---

## trigger_starttimer_ext

Used for spawning a `trigger_starttimer` entity. You must set `mins`, `maxs` and `origin` keys for this manually. Supports same entity keys and spawnflags as regular `target/trigger_starttimer`.

```{hint}
When `g_scriptDebug` is set to **1**, this entitys bounding box will be drawn in blue.
```

---

## trigger_stoptimer_ext

Used for spawning a `trigger_stoptimer` entity. You must set `mins`, `maxs` and `origin` keys for this manually. Supports same entity keys and spawnflags as regular `target/trigger_stoptimer`.

```{hint}
When `g_scriptDebug` is set to **1**, this entitys bounding box will be drawn in blue.
```

---

## usetarget

`usetarget <targetname>`

Activates targeted entities. Same as `alertentity`, but passes the activator data to the target(s).

```{caution}
This script action **must** be called via an entity that passes activator data!
```

---

## wm_announce

`wm_announce <message>`

Prints a popup messages for all players. `%s` can be used to print out activators name.

```{caution}
If using `%s` to print the activators name, you **must** call this via an entity that passes activator data!
```

---

## wm_announce_private

`wm_announce_private <message>`

Prints a popup messages for the activator only. `%s` can be used to print out activators name.

```{caution}
This script action **must** be called via an entity that passes activator data!
```
