# ETJump mapping entities

Here you will find full list of ETJump entities you can use in your map. Included on this list are also stock ET entities that have been expanded or fixed by ETJump.

```{hint}
Entities which originate from ETMain only list the modifications that ETJump offers to the entities. Refer to the entity descriptions in Radiant for a full list of keys and spawnflags.
```

---

## etjump_game_manager

Automatically spawned on a map with no `script_multiplayer` or any entity with a `scriptname` set. Provides access to mapscripting for any map, regardless of existing entities. This is effectively the same as `script_multiplayer`.

**Keys**

| Key        | Value | Default        | Description                   |
| :--------- | :---- | :------------- | :---------------------------- |
| scriptname |       | etjump_manager | Entry point for mapscripting. |

**Spawnflags**

*None*

```{attention}
**Do not** place this entity manually in your map in Radiant! Use `script_multiplayer` instead.
```

---

## etjump203_target_relay

A `target_relay` that works only on **ETJump 2.0.3** and newer.

**Keys**

*None*

**Spawnflags**

*None*

```{caution}
Fires a random target instead of all targets.
```

---

## etjump2_target_relay

A `target_relay` that works only on **ETJump 2.0.0** and newer.

**Keys**

*None*

**Spawnflags**

*None*

```{caution}
Fires a random target instead of all targets.
```

---

## func_button

When a button is used, it moves some distance in the direction of it's angles, triggers all of it's targets, waits some time, then returns to it's original position where it can be triggered again.

**Keys**

| Key   | Value        | Default                         | Description                                                             |
| :---- | :----------- | :------------------------------ | :---------------------------------------------------------------------- |
| noise | path to .wav | sound/movers/switches/butn2.wav | Sound to play on activation. Use `nosound` to disable sound completely. |

**Spawnflags**

*None*

---

## func_invisible_user

Uses targeted entities upon activation.

**Keys**

| Key    | Value        | Default | Description                  |
| :----- | :----------- | :------ | :--------------------------- |
| noise  | path to .wav |         | Sound to play on activation. |
| volume | any integer  | 255     | Volume of activation sound.  |

**Spawnflags**

| Spawnflag | Description                       |
| :-------: | :-------------------------------- |
| 8         | Pass activator data to mapscript. |

---

## func_missilepad

Explodes hand and rifle grenades and fires target(s) upon impact.

**Keys**

| Key    | Value        | Default | Description                                    |
| :----- | :----------- | :------ | :--------------------------------------------- |
| scale  | any value    | 1.0     | Scales the knockback given from the explosion. |
| noise  | path to .wav |         | Sound to play on activation.                   |
| volume | any integer  | 255     | Volume of activation sound.                    |

**Spawnflags**

| Spawnflag | Description                                                                             |
| :-------: | :-------------------------------------------------------------------------------------- |
| 1         | Start the entity as non-existent, if targeted, it will toggle existence when triggered. |
| 2         | Applies `scale` only to horizontal velocity.                                            |
| 4         | Applies `scale` only to vertical velocity.                                              |

```{note}
Only direct impact fires targets, splash damage is ignored.

Activating this entity via another entity or from mapscript with `alertentity/usetarget` does **not** fire targets.
```

---

## func_portaltarget

A brush model that spawns portalgun portals shot on it always on the same position.

**Keys**

*None*

**Spawnflags**

*None*

```{note}
The portals are centered on the plane where they spawn either on an explicit origin set by an origin brush, or using the entity's center position. The shaders used on the surfaces of this entity should have the correct surfaceparms for portals set. Using a separate brush with portal surfaceparms, overlaid on top of this entity is unlikely to work reliably.
```

---

## func_static

A static brushmodel that does nothing by itself. Activates targets when hurt if `PAIN` spawnflag is set.

**Keys**

*None*

**Spawnflags**

| Spawnflag | Description                                                 |
| :-------: | :---------------------------------------------------------- |
| 8         | Disable random **500-1000ms** wait added on top of `delay`. |

---

## target_activate_if_velocity

Activates targeted entities if player's velocity is between the lower and upper velocity limit.

**Keys**

| Key         | Value       | Default | Description                                                 |
| :---------- | :---------- | :------ | :---------------------------------------------------------- |
| lower_limit | any integer | 0       | Fires targets if activators speed is higher than specified. |
| upper_limit | any integer | 0       | Fires targets if activators speed is lower than specified.  |

**Spawnflags**

| Spawnflag | Description                         |
| :-------: | :---------------------------------- |
| 1         | Only check for horizontal velocity. |
| 2         | Only check for vertical velocity.   |

```{caution}
Fires a random target instead of all targets.
```

---

## target_checkpoint and trigger_checkpoint

Timerun checkpoint.

**Keys**

| Key  | Value    | Default | Description          |
| :--- | :------- | :------ | :------------------- |
| name | any text | default | The name of the run. |

**Spawnflags**

*None*

```{note}
Timerun names are case sensitive, and may contain color codes.
```

```{note}
A timerun can have a maximum of **16** checkpoints attached to it.
```

---

## target_give

Gives activator targeted items. Must target actual entites in the map. Standard class restrictions apply when giving weapons (eg. cannot give `weapon_panzerfaust` to a medic).

**Keys**

*None*

**Spawnflags**

*None*

---

## target_ftrelay

Works like `target_relay` but activates the entities for everyone in the player's current fireteam, not just the player.

**Keys**

*None*

**Spawnflags**

*None*

```{caution}
Fires a random target instead of all targets. The target is randomly picked for each fireteam member.
```

---

## target_init

Initalizes player into a freshly spawned state

**Keys**

*None*

**Spawnflags**

| Spawnflag | Description                       |
| :-------: | :-------------------------------- |
| 1         | Keep currennt health.             |
| 2         | Keep current ammo.                |
| 4         | Keep current weapons.             |
| 8         | Keep portal gun.                  |
| 16        | Keep holdable items (objectives). |
| 32        | Keep ident value.                 |
| 64        | Keep tracker value.               |
| 128       | Remove starting weapons.          |

```{note}
Spawnflag **128** has no effect if spawnflag **4** is set.
```

---

## target_interrupt_timerun

Stops any active timerun without setting a record.

**Keys**

*None*

**Spawnflags**

*None*

---

## target_portal_relay

Fires targets if activator has fired less or equal amount of portals than specified after last portal reset.

**Keys**

| Key        | Value       | Default | Description                                                              |
| :--------- | :---------- | :------ | :----------------------------------------------------------------------- |
| maxportals | any integer | -100      | Maximum number of portals client is allowed to fire to activate targets. |

**Spawnflags**

*None*

---

## target_print

Prints `message` as a centerprint. If no spawnflags are specified, prints to all clients, including spectators.

**Keys**

*None*

**Spawnflags**

| Spawnflag | Description                                                  |
| :-------: | :----------------------------------------------------------- |
| 8         | Prints to popup rather than centerprint.                     |
| 16        | Replace `[n]` or `%s` in `message` with the activators name. |

---

## target_push

Pushes activator towards `target` or `angle(s)`.

**Keys**

*None*

**Spawnflags**

| Spawnflag | Description                   |
| :-------: | :---------------------------- |
| 2         | Horizontal speed is additive. |
| 4         | Vertical speed is additive.   |

---

## target_relay

Fires its targets when activated.

**Keys**

*None*

**Spawnflags**

| Spawnflag | Description                                         |
| :-------: | :-------------------------------------------------- |
| 8         | Only fires targets if activator is timerunning.     |
| 16        | Only fires targets if activator is not timerunning. |

---

## target_remove_portals

Removes activators existing portals.

**Keys**

| Key    | Value        | Default | Description                               |
| :----- | :----------- | :------ | :---------------------------------------- |
| noise  | path to .wav | nosound | WAV file to play when portal are removed. |
| volume | any integer  | 255     | Volume of the activation sound.           |

**Spawnflags**

| Spawnflag | Description                                |
| :-------: | :----------------------------------------- |
| 1         | Don't print text when portals are removed. |
| 2         | Fire targets when portals are removed.     |

---

## target_save

Saves current position to activators save slot **0**.

**Keys**

*None*

**Spawnflags**

*None*

---

## target_savereset and trigger_savereset

Resets activators saved positions.

**Keys**

*None*

**Spawnflags**

| Spawnflag | Description                            |
| :-------: | :------------------------------------- |
| 1         | Don't print text when saves are reset. |

---

## target_scale_velocity

Scales activator's velocity.

**Keys**

| Key   | Value       | Default | Description                                                         |
| :---- | :---------- | :------ | :------------------------------------------------------------------ |
| scale | any value   | 1.0     | Scaling factor for activators speed.                                |
| time  | any integer | 0       | Time in seconds for constant speed scale when `spawnflag 1` is set. |

**Spawnflags**

| Spawnflag | Description                                         |
| :-------: | :-------------------------------------------------- |
| 1         | Scale base movement speed instead of current speed. |

```{note}
When `spawnflag 1` is set, `scale` is limited to **0.25 - 3.0**.
```

---

\## target_set_health
Sets activators health to specified value.

**Keys**

| Key    | Value                | Default | Description                                                   |
| :----- | :------------------- | :------ | :------------------------------------------------------------ |
| health | any positive integer | 100     | Value to set health to.                                       |
| wait   | any integer          | 1000    | Delay in milliseconds between activations by the same player. |

**Spawnflags**

| Spawnflag | Description                  |
| :-------: | :--------------------------- |
| 1         | Activate only once per life. |

---

## target_starttimer and trigger_starttimer

Starts a timerun for the activator.

**Keys**

| Key         | Value     | Default | Description                                                 |
| :---------- | :-------- | :------ | :---------------------------------------------------------- |
| name        | any text  | default | Name of the run.                                            |
| speed_limit | any value | 700     | Maximum speed the activator can have when starting the run. |

**Spawnflags**

| Spawnflag | Description                                          |
| :-------: | :--------------------------------------------------- |
| 1         | Run resets on team change.                           |
| 2         | Run resets on death.                                 |
| 4         | Run resets only wnen reaching the end.               |
| 8         | Run resets if client sets `pmove_fixed 0`.           |
| 16        | Disables `backup` and extra save slots.              |
| 32        | Cannot pickup explosive weeapons.                    |
| 64        | Cannot pickup portal gun.                            |
| 128       | Disables `save`, run is reset if client uses `load`. |

By default, timeruns are reset on team change, death, or if client sets `pmove_fixed 0`. If **ANY** spawnflags are set, you must explicitly specify the reset conditions.

Runs that don't reset on team change are still reset if the player goes to spectate.

Starting a timerun performs the following actions to the activating player:

- Removes explosive weapons and flamethrower
- Removes all projectiles and mines of the activator
- Removes portalgun
- Resets portals
- Clears all save slots and backups (unless `spawnflag 128` is set) that were made during a previous timerun.

```{note}
`speed_limit` is absolute total velocity in all directions, not just horizontal velocity.
```

```{note}
Timerun names are case sensitive, and may contain color codes.
```

---

## target_stoptimer and trigger_stoptimer

Stops a timerun for the activator.

**Keys**

| Key  | Value    | Default | Description      |
| :--- | :------- | :------ | :--------------- |
| name | any text | default | Name of the run. |

**Spawnflags**

*None*

```{note}
Timerun names are case sensitive, and may contain color codes.
```

---

## target_teleporter and trigger_teleport

Teleports player to target location.

**Keys**

| Key      | Value        | Default | Description                                           |
| :------- | :----------- | :------ | :---------------------------------------------------- |
| outspeed | any integer  | 0       | Fixed speed at which activators exits the teleporter. |
| noise    | path to .wav | nosound | Sound to play on activation.                          |

**Spawnflags**

| Spawnflag | Description                                                                            |
| :-------: | :------------------------------------------------------------------------------------- |
| 1         | Reset activators speed.                                                                |
| 2         | Convert activators speed towards destination angles.                                   |
| 4         | Convert angle and speed relative to destination while preserving yaw angle.            |
| 8         | Convert angle and speed relative to destination while preserving yaw and pitch angles. |
| 16        | Apply **160ms** long knockback event after teleportation (Quake 3 behavior).           |

---

## target_tracker and trigger_tracker

Activates entities conditionally based on activators "tracker values". This is mainly meant to be used for tracking map progression, but it can have other use cases too. Replacement for `target_activate` and entities related to that.

There are three different formats for specifying the tracker index and value.

1. `<value>` Set the tracker on index **1** to `<value>`
2. `<index,value>` Set the tracker on index `<index>` to `<value>`
3. `<index1,value1>|<index2,value2>|..|<indexN,valueN>` Set the trackers on indices `<index1, index2, .., indexN>` to values `<value1, value2, .., valueN>`

```{note}
Valid range for tracker indices is **1 - 50**.
```

**Keys**

| Key                 | Value                | Default | Description                                                                                                                                              |
| :------------------ | :------------------- | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| tracker_eq          | *see examples below* |         | Tracker activates targets if specified tracker value matches the player's tracker value.                                                                 |
| tracker_not_eq      | *see examples below* |         | Tracker activates targets if specified tracker value does not match the player's tracker value.                                                          |
| tracker_gt          | *see examples below* |         | Tracker activates targets if player's tracker value is greater than specified value.                                                                     |
| tracker_lt          | *see examples below* |         | Tracker activates targets if player's tracker value is less than the specified value.                                                                    |
| tracker_set         | *see examples below* |         | Tracker sets player's tracker value to the specified value.                                                                                              |
| tracker_set_if      | *see examples below* |         | Tracker sets player's tracker value to the specified value if conditions from `tracker_eq`, `tracker_not_eq`, `tracker_gt` or `tracker_lt` are met.      |
| tracker_inc         | *see examples below* |         | Tracker increases player's tracker value by the specified value.                                                                                         |
| tracker_inc_if      | *see examples below* |         | Tracker increases player's tracker value by the specified value if conditions from `tracker_eq`, `tracker_not_eq`, `tracker_gt` or `tracker_lt` are met. |
| tracker_bit_set     | *see examples below* |         | Tracker sets players tracker bit to specified value.                                                                                                     |
| tracker_bit_reset   | *see examples below* |         | Tracker resets players tracker bit.                                                                                                                      |
| tracker_bit_is_set  | *see examples below* |         | Tracker activates targets if player's tracker bit is set.                                                                                                |
| tracker_bit_not_set | *see examples below* |         | Tracker activates targets if player's tracker bit is not set.                                                                                            |

**Spawnflags**

*None*

### Examples

Set players tracker values.

| Key         | Value         | Explanation                                   |
| :---------- | :------------ | :-------------------------------------------- |
| tracker_set | 5             | Set tracker value on index 1 to 5             |
| tracker_set | 2,5           | Set tracker value on index 2 to 5             |
| tracker_set | 1,5\|2,5\|3,5 | Set tracker values on indices 1, 2 and 3 to 5 |

---

Check players tracker values and activate targeted entities if conditions are met.

| Key        | Value         | Explanation                                                                 |
| :--------- | :------------ | :-------------------------------------------------------------------------- |
| tracker_eq | 5             | Tracker value on index 1 must be 5. If true, activates targets.             |
| tracker_eq | 2,5           | Tracker value on index 2 must be 5. If true, activates targets.             |
| tracker_eq | 1,5\|2,5\|3,5 | Tracker values on indices 1, 2 and 3 must be 5. If true, activates targets. |

---

Check players tracker values, fire targetsed entities if conditions are met and modify the players tracker values afterwards.

```{eval-rst}
+----------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keys           | Value        | Explanation                                                                                                                                                                           |
+================+==============+=======================================================================================================================================================================================+
| tracker_eq     | 4            | Tracker value on index 1 must be 4. If true, activates targets and sets players tracker value on index 1 to 5.                                                                        |
+----------------+--------------+                                                                                                                                                                                       |
| tracker_set_if | 5            |                                                                                                                                                                                       |
+----------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tracker_gt     | 2,2          | Tracker value on index 1 must greater than 2. If true, activates targets and sets players tracker value on index 4 to 5.                                                              |
+----------------+--------------+                                                                                                                                                                                       |
| tracker_set_if | 4,5          |                                                                                                                                                                                       |
+----------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tracker_not_eq | 1,2|2,2|3,2  | Tracker values on indices 1, 2 and 3 must not be 2. If true, activates targets and increases tracker value on index 1 by 1, index 2 by 5 and decreases tracker value on index 3 by 2. |
+----------------+--------------+                                                                                                                                                                                       |
| tracker_inc_if | 1,1|2,5|3,-2 |                                                                                                                                                                                       |
+----------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

```{note}
`tracker_not_eq` acts as an "or" condition, meaning if specifying multiple indices, none of the specified values can match the activators tracker values.
```

---

## trigger_push

Pushes activator towards `target` or `angle(s)`. This entity is client side predicted.

**Keys**

| Key   | Value        | Default | Description                                                         |
| :---- | :----------- | :------ | :------------------------------------------------------------------ |
| speed | any integer  | 1000    | Speed at which player is launched. No effect if aimed at an entity. |
| noise | path to .wav | nosound | Sound to play on activation.                                        |
| wait  | any integer  | 100     | Milliseconds to wait before re-activation.                          |

**Spawnflags**

| Spawnflag | Description                   |
| :-------: | :---------------------------- |
| 2         | Horizontal speed is additive. |
| 4         | Vertical speed is additive.   |

---

## weapon_grenadelauncher

Spawns an Axis hand grenade at the location.

**Keys**

| Key   | Value       | Default | Description             |
| :---- | :---------- | :------ | :---------------------- |
| count | any integer | 0       | Amount of ammo to give. |

**Spawnflags**

| Spawnflag | Description                                                     |
| :-------: | :-------------------------------------------------------------- |
| 1         | Spawns on the entitys location and does not fall to the ground. |
| 4         | Bobs up and down.                                               |

```{note}
Unlike other `weapon_` entities, this respects the maximum grenade limits of classes.
```

---

## weapon_grenadepineapple

Spawns an Allied hand grenade at the location.

**Keys**

| Key   | Value       | Default | Description             |
| :---- | :---------- | :------ | :---------------------- |
| count | any integer | 0       | Amount of ammo to give- |

**Spawnflags**

| Spawnflag | Description                                                     |
| :-------: | :-------------------------------------------------------------- |
| 1         | Spawns on the entitys location and does not fall to the ground. |
| 4         | Bobs up and down.                                               |

```{note}
Unlike other `weapon_` entities, this respects the maximum grenade limits of classes.
```

---

## weapon_portalgun

Spawns a portal gun at the location.

**Keys**

*None*

**Spawnflags**

| Spawnflag | Description             |
| :-------: | :---------------------- |
| 2         | Spins around it's axis. |
| 4         | Bobs up and down.       |

```{note}
Unlike other `weapon_` entities, this entity does not fall to the ground.
```

```{tip}
This entity does not disappear when picked up, and does not need to be manually respawned like other `weapon_` entities.
```

---

## worldspawn

**Keys**

| Key             | Value             | Default | Description                                                                                                                                                                           |
| :-------------- | :---------------- | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| nodrop          | 0 or  1           | 0       | Enable/disable nodrop. **0** Items are not dropped inside `surfaceparm nodrop`. **1** items are only dropped inside `surfaceparm nodrop`.                                             |
| noexplosives    | 0 - 2             | 0       | Disables explosives. **0** explosives are allowed. **1** no explosive weapons. **2** no dynamite.                                                                                     |
| nofalldamage    | 0 - 2             | 0       | Enable/disable fall damage. **0** Fall damage disabled only on `surfaceparm nodamage` **1** Fall damage enabled only on `surfaceparm nodamage` **2** Fall damage disabled everywhere. |
| noghost         | 0 or 1            | 0       | Disables player ghosting (nonsolid players). Overrides `g_ghostPlayers` server cvar.                                                                                                  |
| nogod           | 0 or 1            | 0       | Disables god mode.                                                                                                                                                                    |
| nogoto          | 0 or 1            | 0       | Disables goto.                                                                                                                                                                        |
| nojumpdelay     | 0 or 1            | 0       | Enable/disable jump delay. **0** No jump delay only on `surfaceparm monsterslicknorth` **1** Jump delay only on `surfaceparm monsterslicknorth`.                                      |
| nonoclip        | 0 or 1            | 0       | Enable/disable noclip. **0** Don't allow noclip inside `surfaceparm donotenterlarge` **1** Only allow noclip inside `surfaceparm donotenterlarge`.                                    |
| nosave          | 0 or 1            | 0       | Enable/disable save. **0** Don't allow save inside `surfaceparm clusterportal` brushes **1** Only allow save inside `surfaceparm clusterportal` brushes.                              |
| nooverbounce    | 0 or 1            | 0       | Enable/disable overbounces. **0** Don't allow overbounces on `surfaceparm monsterslicksouth` **1** Only allow overbounces on `surfaceparm monsterslicksouth`.                         |
| noprone         | 0 or 1            | 0       | Enable/disable prone. **0** Don't allow prone inside `surfaceparm donotenter` brushes **1** Only allow prone inside `surfaceparm donotenter` brushes.                                 |
| nowallbug       | 0 or 1            | 0       | Toggles whether players can accelerate while stuck in a wall.                                                                                                                         |
| portalgun_spawn | 0 or 1            | 0       | Toggles whether players should spawn with a portal gun.                                                                                                                               |
| portalsurfaces  | 0 or 1            | 1       | Enable/disable portalsurfaces. **0** Only allow portals on `surfaceparm monsterslickeast` **1** Don't allow portals on `surfaceparm monsterslickeast`.                                |
| portalteam      | 0 - 2             | 0       | If set to **0**, players can only go to own portals. If set to **1**, players can also go to fireteam mates' portals. If set to **2**, anyone can go to anyones portals.              |
| limitedsaves    | any integer       | 0       | If set to higher than 0, saves are limited to the set value.                                                                                                                          |
| strictsaveload  | bitflag or string | 0       | Limits save and load by given conditions. **1/move** cannot save while moving **2/dead** cannot save/load while dead. Combine strings with `\|` (eg. `move \| dead`).                 |

**Spawnflags**

*None*

---

## Deprecated entities

These entities are considered deprecated, and while still functional, usage is discouraged.

---

### target_activate

**Reason for deprecation**

Replaced by [target_tracker and trigger_tracker](#target_tracker-and-trigger_tracker).

---

Activates targeted entities if ident requirement is set.

**Keys**

| Key      | Value       | Default | Description                          |
| :------- | :---------- | :------ | :----------------------------------- |
| reqident | any integer | 0       | Ident value required for activation. |

**Spawnflags**

| Spawnflag | Description                                                        |
| :-------: | :----------------------------------------------------------------- |
| 1         | Fires targets if activators ident value is greater than `reqident` |
| 2         | Fires targets if activators ident value is not `reqident`          |
| 4         | Fires targets if activators ident value is less than `reqident`    |

```{note}
Default behavior is to fire targets if ident is equal to `reqident`.
```

```{caution}
Fires a random target instead of all targets.
```

---

### target_decay

**Reason for deprecation**

Replaced by [target_tracker and trigger_tracker](#target_tracker-and-trigger_tracker).

---

Decays activators ident value.

**Keys**

| Key         | Value       | Default | Description                                                              |
| :---------- | :---------- | :------ | :----------------------------------------------------------------------- |
| ident       | any integer | -1      | Ident value required for activation.                                     |
| decay_time  | any integer | -1      | How long in milliseconds it takes for ident to decay to specified value. |
| decay_value | any integer | -1      | Value to which ident decays to.                                          |

**Spawnflags**

*None*

---

### target_increase_ident

**Reason for deprecation**

Replaced by [target_tracker and trigger_tracker](#target_tracker-and-trigger_tracker).

---

Increases the players map progression identifier.

**Keys**

| Key | Value       | Default | Description                                                                   |
| :-- | :---------- | :------ | :---------------------------------------------------------------------------- |
| inc | any integer | 1       | How much the identifier should be increased when player activates the entity. |

**Spawnflags**

*None*

---

### target_printname

**Reason for deprecation**

[target_print](#target_print) provides all the same functionality as this entity.

---

Prints `message` as a popup message. If no spawnflags are specified, prints to all clients, including spectators.

| Key     | Value      | Default | Description                                                      |
| :------ | :--------- | :------ | :--------------------------------------------------------------- |
| message | any string |         | Message to print. `%s` can be used to print the activators name. |

**Spawnflags**

| Spawnflag | Description                   |
| :-------: | :---------------------------- |
| 1         | Only print for Axis.          |
| 2         | Only print for Allies.        |
| 4         | Only print for the activator. |

---

### target_setident

**Reason for deprecation**

Replaced by [target_tracker and trigger_tracker](#target_tracker-and-trigger_tracker).

---

Sets the activator's map progression identifier.

**Keys**

| Key   | Value       | Default | Description                              |
| :---- | :---------- | :------ | :--------------------------------------- |
| ident | any integer | 0       | The value the identifier will be set to. |

**Spawnflags**

*None*

---

### trigger_multiple spawnflags 512 & 2048

**Reason for deprecation**

Since ETJump 3.1.0, the `spawnflags 2048` behavior was made the default. `spawnflags 512` has been deprecated as it never provided any new functionality, as it effectively just set `wait` to `1000 / sv_fps`.

---

Activates targets when touched.

**Keys**

*None*

**Spawnflags**

| Spawnflag | Description                                                 |
| :-------: | :---------------------------------------------------------- |
| 512       | Activates every server frame.                               |
| 2048      | Acitavtes for all touching clients with unique wait cycles. |
