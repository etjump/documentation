# ETJump Map Scripting

ETJump adds new scripting actions, events and entities for mapscripting. Below is a list of new scripting actions, as well as any additions to existing ones.

## create
```
create
{
    <entity keys>
}
```

_Disclaimer: the documentation of this script action is possibly lacking and inaccurate._

Allows limited spawning of entities in a map. `create` should be called as a first thing inside `game_manager` -> `spawn` scriptblock. If a map lacks `script_multiplayer` or the `game_manager` script block, it should be called at another entitys `spawn` block, preferrably one that has no brushwork (eg. a point entity). Each entity must be given `classname` and `origin` keys, and additionally for `trigger_multiple_ext`, `trigger_starttimer_ext`, `trigger_checkpoint_ext`, `trigger_stoptimer_ext` and `func_fakebrush`, the brushmodel `mins` and `maxs` (and `contents` in case of `func_fakebrush`). Spawning of point entities generally works as if you would make them in map editor (just remember to set `origin` key manually), but spawning of brush entities is severly limited. Such limits include, but are not necessarily limited to:

* Only brush entities that function when spawned out of nothing are `trigger_multiple`, ` trigger_multiple_ext`, `trigger_starttimer_ext`, `trigger_checkpoint_ext`, `trigger_stoptimer_ext`, `trigger_push`, and `func_fakebrush`. Any other brush entity will spawn, but won't function properly unless a brushmodel is hijacked from another entity in the map.
* Only `trigger_multiple_ext`, `trigger_starttimer_ext`, `trigger_checkpoint_ext`, `trigger_stoptimer_ext` and `func_fakebrush` can create volume by setting `mins/maxs`, others act as point entities unless hijacking a brushmodel from another entity in the map.
* Spawning of visible brushwork only works by hijacking another brushmodel from a map; it's not possible to create your own, visible brushmodel with specific textures.
* You cannot set surfaceparms, only contentparms can be modified with `contents <integer>` key (see [surfaceflags.h](https://github.com/etjump/etjump/blob/091acf0658605061441aa8bc0268fe96290f8315/src/game/surfaceflags.h#L13-L39)).
    * Some contentparms are compile-time only, such as `CONTENTS_LIGHTGRID` and `CONTENTS_AREAPORTAL`, and cannot be used.

### Hijacking brushmodels

To hijack an existing brushmodel from a map, use the `model "*N"` key, where `N` corresponds to the number of the brushmodel you want to hijack. To find out this number, open the BSP file of the map in any text editor and find the brushmodel you want to hijack, and check the model number (eg. `model "*12"`). Hijacking existing brushmodels is the only way to create visible brush entities, and the only way to define `mins/maxs` for a created brushmodel (apart from `trigger_multiple_ext` and `func_fakebrush`).

Considerations with brushmodel hijacking:

* If the brushmodel you are hijacking is visible at the same time as the entity you are hijacking it to, either might become invisible.
* When setting the `origin` key, the value is relative to the brushmodel you are hijacking, meaning you are moving the brushmodel from its original postion rather than setting an absolute position.
* Hijacking another brushmodel does not remove the original, but rather duplicates it. This means that it's possible to hijack same brushmodel multiple times for different entities.

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

Creating a trigger which activates a print.

```
game_manager
{
    spawn
    {
        create
        {
            classname "trigger_multiple_ext"
            origin "224 -96 40"
            mins "-32 -32 -32"
            maxs "32 32 32"
            target "print"
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

`cvar [cvarname] set/inc/random [value]`

These mapscript actions have been removed from ETJump as they can be used for malicious purposes, e.g. changing `rconPassword` on server.

---

## damageplayer
`damageplayer <damage>`

Damages player by given amount. Damage is halved if the player has `etj_nofatigue 1` due to it giving player constant adrenaline.

_Note: This script action **must** be called via `target_script_trigger` entity to pass activator data._

---

## etjump_manager

Acts as an entry point for mapscript. If a map contains no `script_multiplayer` or any entities with a `scriptname` set, you can use this script block to access mapscripting in a map, e.g. spawn in entities using [create](#create). This is only present in maps which do not provide `script_multiplayer` or entities with a `scriptname` set.

---

## func_fakebrush

`func_fakebrush` is a special brush entity that can be spawned via mapscripts. Historically it is used in ETPro to fix exploits in maps. It can act as a clip brush for example to prevent players from jumping out of the map, if the mapper has failed to clip the map properly. To spawn a `func_fakebrush`, you must set the following keys: `origin`, `mins`, `maxs` and `contents`.

_Note: when `g_scriptDebug` is set to **1**, this entitys bounding box will be drawn in red._

---

## killplayer
`killplayer`

Kills the player as if they used `/kill` command.

_Note: This script action **must** be called via `target_script_trigger` entity to pass activator data._

---

## setplayerautospawn
`setplayerautospawn <objective description>`

Sets the activating players auto spawnpoint to specified spawnpoint. `objective description` is the `description` key of `team_WOLF_objective` (visible next to the clickable flag on command map). Spawnpoint name must be inside quotes if it contains spaces (eg. `setplayerautospawn "Forward Bunker"`).

_Note: This script action **must** be called via `target_script_trigger` entity to pass activator data._

---

## setplayerspawn
`setplayerspawn <objective description>`

Sets the activating players current spawnpoint to specified spawnpoint. `objective description` is the `description` key of `team_WOLF_objective` (visible next to the clickable flag on command map). Spawnpoint name must be inside quotes if it contains spaces (eg. `setplayerspawn "Forward Bunker"`).

_Note: This script action **must** be called via `target_script_trigger` entity to pass activator data._

---

## trigger_checkpoint_ext

Used for spawning a `trigger_checkpoint` entity. You must set `mins`, `maxs` and `origin` keys for this manually. Supports same entity keys and spawnflags as regular `target/trigger_checkpoint`.

_Note: when `g_scriptDebug` is set to **1**, this entitys bounding box will be drawn in magenta._

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

_Note: when `g_scriptDebug` is set to **1**, this entitys bounding box will be drawn in green._

---

## trigger_starttimer_ext

Used for spawning a `trigger_starttimer` entity. You must set `mins`, `maxs` and `origin` keys for this manually. Supports same entity keys and spawnflags as regular `target/trigger_starttimer`.

_Note: when `g_scriptDebug` is set to **1**, this entitys bounding box will be drawn in blue._

---

## trigger_stoptimer_ext

Used for spawning a `trigger_stoptimer` entity. You must set `mins`, `maxs` and `origin` keys for this manually. Supports same entity keys and spawnflags as regular `target/trigger_stoptimer`.

_Note: when `g_scriptDebug` is set to **1**, this entitys bounding box will be drawn in blue._

---
