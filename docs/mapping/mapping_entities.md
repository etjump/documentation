# ETJump mapping entities
Here you will find full list of ETJump entities you can use in your map. Included on this list are also stock ET entities that have been expanded or fixed by ETJump.

## etjump_game_manager
Automatically spawned on a map with no `script_multiplayer` or any entity with a `scriptname` set. Provides access to mapscripting for any map, regardless of existing entities. This entity is not meant to be placed by a mapper, it's automatically spawned by the game if necessary. This is effectively the same as `script_multiplayer`.

**Keys**

Key              | Values            | Default            | Description
-----------------|:-----------------:|--------------------|------------
scriptname       |                   | etjump_manager     | Entry point for mapscripting.

**Spawnflags:**
_None_

---

## etjump203_target_relay
A `target_relay` that works only on **ETJump 2.0.3** and newer.

**Keys:**
_None_

**Spawnflags:**
_None_

_Note: Fires a random target instead of all targets._

---

## etjump2_target_relay
A `target_relay` that works only on **ETJump 2.0.0** and newer.

**Keys:**
_None_

**Spawnflags:**
_None_

_Note: Fires a random target instead of all targets._

---

## func_button
When a button is used, it moves some distance in the direction of it's angles, triggers all of it's targets, waits some time, then returns to it's original position where it can be triggered again.

**Keys**

Key              | Values            | Default                         | Description
-----------------|:-----------------:|---------------------------------|------------
noise            | path to .wav      | sound/movers/switches/butn2.wav | Sound to play on activation. Use `nosound` to disable sound completely.

**Spawnflags:**
_None_

---

## func_invisible_user
Uses targeted entities on activation.

**Keys**

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
noise            | path to .wav      |               | Sound to play on activation.
volume           | any integer       | 255           | Volume of activation sound.

**Spawnflags:**

Spawnflag  | Description
:---------:|:-----------
8          | Pass activator data to mapscript.

---

## func_missilepad
Explodes hand and rifle grenades and fires target(s) upon impact.

**Keys**

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
scale            | any value         | 1.0           | Scales the knockback given from the explosion.
noise            | path to .wav      |               | Sound to play on activation.
volume           | any integer       | 255           | Volume of activation sound.

**Spawnflags:**

Spawnflag  | Description
:---------:|:-----------
1          | Start the entity as non-existent, if targeted, it will toggle existence when triggered.
2          | Applies `scale` only to horizontal velocity.
4          | Applies `scale` only to vertical velocity.

_Note: Only direct impact fires targets, splash damage is ignored. Using this entity does not fire targets._

---

## func_portaltarget
A brush model that spawns portalgun portals shot on it always on the same position.

**Keys**
_None_

**Spawnflags:**
_None_

_Note: The portals are centered on the plane where they spawn either on an explicit origin set by an origin brush, or using the entity's center position. The surfaces should have the correct surfaceparm directly. Due to how traces work with bmodels, using a separate portalsurface-brush is unlikely to work._

---

## func_static
Uses targeted entities on activation.

**Keys:**
_None_

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
8          | Disable random **500-1000ms** wait added on top of `delay`.

---

## target_activate_if_velocity
Activates targeted entities if player's velocity is between the lower and upper velocity limit.

**Keys**

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
lower_limit      | any integer       | 0             | Fires targets if activators speed is higher than specified.
upper_limit      | any integer       | 0             | Fires targets if activators speed is lower than specified.

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
1          | Only check for horizontal velocity.
2          | Only check for vertical velocity.

_Note: Fires a random target instead of all targets._

---

## target_checkpoint and trigger_checkpoint
Timerun checkpoint.

**Keys**

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
name             | any text          | default       | The name of the run. Names are case sensitive.

**Spawnflags:**
_None_

A timerun can have a maximum of **16** checkpoints.

---

## target_give
Gives activator targeted items. Must target actual entites in the map. Standard class restrictions apply when giving weapons (eg. cannot give `weapon_panzerfaust` to a medic).

**Keys:**
_None_

**Spawnflags:**
_None_

---

## target_ftrelay
Works like `target_relay` but activates the entities for everyone in the player's current fireteam, not just the player.

**Keys:**
_None_

**Spawnflags:**
_None_

_Note: Fires a random target instead of all targets. The target is randomly picked for each fireteam member._

---

## target_init
Initalizes player into a freshly spawned state

**Keys:**
_None_

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
1          | Keep currennt health.
2          | Keep current ammo.
4          | Keep current weapons.
8          | Keep portal gun.
16         | Keep holdable items (objectives).
32         | Keep ident value.
64         | Keep tracker value.
128        | Remove starting weapons.

_Note: spawnflags **128** has no effect if spawnflags **4** is used._

---

## target_interrupt_timerun
Stops any active timerun without setting a record.

**Keys:**
_None_

**Spawnflags:**
_None_

---

## target_portal_relay
Fires targets if activator has fired less or equal amount of portals than specified after last portal reset.

**Keys**

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
maxportals       | any integer       | -1            | Maximum number of portals client is allowed to fire to activate targets.

**Spawnflags:**
_None_

---

## target_print
Prints `message` as a centerprint. If no spawnflags are specified, prints to all clients, including spectators.

**Keys:**
_None_

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
8          | Prints to popup rather than centerprint.
16         | Replace `[n]` or `%s` in `message` with the activators name.

---

## target_push
Pushes activator towards `target` or `angle(s)`.

**Keys:**
_None_

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
2          | Horizontal speed is additive.
4          | Vertical speed is additive.

---

## target_relay
Fires its targets when activated.

**Keys:**
_None_

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
8          | Only fires targets if activator is timerunning.
16         | Only fires targets if activator is not timerunning.

---

## target_remove_portals
Removes activators existing portals.

**Keys**

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
noise            | path to .wav      | nosound       | WAV file to play when portal are removed.
volume           | any integer       | 255           | Volume of the activation sound.

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
1          | Don't print text when portals are removed.
2          | Fire targets when portals are removed.

---

## target_save
Saves current position to activators save slot **0**.

**Keys:**
_None_

**Spawnflags:**
_None_

---

## target_savereset and trigger_savereset
Resets activators saved positions.

**Keys:**
_None_

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
1          | Don't print text when saves are reset.

---

## target_scale_velocity
Scales activator's velocity.

**Keys**

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
scale            | any value         | 1.0           | Scaling factor for activators speed.
time             | any integer       | 0             | Time in seconds for constant speed scale when `spawnflags 1` is set.

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
1          | Scale base movement speed instead of current speed.

_Note: When `spawnflags 1` is used, `scale` is limited to **0.25 - 3.0**_

---

## target_set_health
Sets activators health to specified value.

**Keys**

Key              | Values               | Default       | Description
-----------------|:--------------------:|---------------|------------
health           | any positive integer | 100           | Value to set health to.
wait             | any integer          | 1000          | Delay in milliseconds between activations by the same player.

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
1          | Activate only once per life.

---

## target_starttimer and trigger_starttimer
Starts a timerun for the activator.

**Keys**

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
name             | any text          | default       | Name of the run.
speed_limit      | any value         | 700           | Maximum speed the activator can have when starting the run.

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
1          | Run resets on team change.
2          | Run resets on death.
4          | Run resets only wnen reaching the end.
8          | Run resets if client sets `pmove_fixed 0`.
16         | Disables `backup` and extra save slots.
32         | Cannot pickup explosive weeapons.
64         | Cannot pickup portal gun.
128        | Disables `save`, run is reset if client uses `load`.

By default, timeruns are reset on team change, death and if client sets `pmove_fixed 0`. If **ANY** spawnflags are set, you must explicitly specify the reset conditions.

Runs that don't reset on team change are still reset if the player goes to spectate.

Starting a timerun performs the following actions to the activating player:

* Removes explosive weapons and flamethrower
* Removes all projectiles and mines of the activator
* Removes portalgun
* Resets portals
* Clears all save slots and backups (unless `spawnflags 128` is used) that were made during a previous timerun.

---

## target_stoptimer and trigger_stoptimer
Stops a timerun for activator.

**Keys**

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
name             | any text          | default       | Name of the run.

**Spawnflags:**
_None_

---

## target_teleporter and trigger_teleport
Teleports player to target location.

**Keys**

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
outspeed         | any integer       | 0             | Fixed speed at which activators exits the teleporter.
noise            | path to .wav      | nosound       | Sound to play on activation.

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
1          | Reset activators speed.
2          | Convert activators speed towards destination angles.
4          | Convert angle and speed relative to destination while preserving yaw angle.
8          | Convert angle and speed relative to destination while preserving yaw and pitch angles.
16         | Apply **160ms** long knockback event after teleportation (Q3 behavior).

---

## target_tracker and trigger_tracker
Replacement for target_activate.

There are three different formats for specifying the tracker index and value.

1. `[value]` Set the tracker on index **1** to `[value]`
2. `[index,value]` Set the tracker on index `[index]` to `[value]`
3. `[index1,value1]|[index2,value2]|..|[indexN,valueN]` Set the trackers on indices `[index1, index2, .., indexN]` to values `[value1, value2, .., valueN]``

Valid range for tracker indices is **1 - 50**.

**Examples**

Key              | Values                | Meaning
-----------------|:---------------------:|----------
tracker_eq       | 1                     | tracker on index 1 has to be 1
tracker_eq       | 2,1                   | tracker on index 2 has to be 1
tracker_eq       | 1,1&#124;2,1&#124;3,1 | trackers on indices 1, 2 and 3 have to be 1

**Keys**

Key                 | Values            | Default       | Description
--------------------|:-----------------:|---------------|------------
tracker_eq          | [index,value]     |               | Tracker activates targets if specified tracker value matches the player's tracker value.
tracker_not_eq      | [index,value]     |               | Tracker activates targets if specified tracker value does not match the player's tracker value.
tracker_gt          | [index,value]     |               | Tracker activates targets if player's tracker value is greater than specified value.
tracker_lt          | [index,value]     |               | Tracker activates targets if player's tracker value is less than the specified value.
tracker_set         | [index,value]     |               | Tracker sets player's tracker value to the specified value.
tracker_set_if      | [index,value]     |               | Tracker sets player's tracker value to the specified value if conditions from `tracker_eq`, `tracker_not_eq`, `tracker_gt` or `tracker_lt` are met.
tracker_inc         | [index,value]     |               | Tracker increases player's tracker value by the specified value.
tracker_inc_if      | [index,value]     |               | Tracker increases player's tracker value by the specified value if conditions from `tracker_eq`, `tracker_not_eq`, `tracker_gt` or `tracker_lt` are met.
tracker_bit_set     | [index,value]     |               | Tracker sets players tracker bit to specified value.
tracker_bit_reset   | [index,value]     |               | Tracker resets players tracker bit.
tracker_bit_is_set  | [index,value]     |               | Tracker activates targets if player's tracker bit is set.
tracker_bit_not_set | [index,value]     |               | Tracker activates targets if player's tracker bit is not set.

**Spawnflags:**
_None_

_Note: `tracker_not_eq` acts as an "or" stamement, meaning if specifying multiple indices, none of the specified values can match the activators tracker values._

---

## trigger_push
Pushes activator towards `target` or `angle(s)`. This entity is client side predicted.

**Keys**

Key              | Values            | Default       | Description
-----------------|:-----------------:|:-------------:|------------
speed            | any integer       | 1000          | Speed at which player is launched. No effect if aimed at an entity.
noise            | path to .wav      | nosound       | Sound to play on activation.
wait             | any integer       | 100           | Milliseconds to wait before re-activation.

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
2          | Horizontal speed is additive.
4          | Vertical speed is additive.

---

## weapon_grenadelauncher
Spawns an Axis hand grenade at the location.

**Keys:**

Key              | Values            | Default       | Description
-----------------|:-----------------:|:-------------:|------------
count            | any integer       | 0             | Amount of ammo to give

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
1          | Spawns on the entitys location and does not fall to the ground.
4          | Bobs up and down.

_Note: unlike other weapon entities, this respects the maximum grenade limits of classes._

---

## weapon_grenadepineapple
Spawns an Allied hand grenade at the location.

**Keys:**

Key              | Values            | Default       | Description
-----------------|:-----------------:|:-------------:|------------
count            | any integer       | 0             | Amount of ammo to give

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
1          | Spawns on the entitys location and does not fall to the ground.
4          | Bobs up and down.

_Note: unlike other weapon entities, this respects the maximum grenade limits of classes._

---

## weapon_portalgun
Spawns a portal gun at the location.

**Keys:**
_None_

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
2          | Spins around it's axis.
4          | Bobs up and down.

_Note: this entity does not fall to the ground._

---

## Worldspawn

**Keys**

Key              | Values            | Default       | Description
-----------------|:-----------------:|:-------------:|------------
nodrop           | 0 or  1           | 0             | Enable/disable nodrop. **0** Items are not dropped inside `surfaceparm nodrop`. **1** items are only dropped inside `surfaceparm nodrop`.
noexplosives     | 0 - 2             | 0             | Disables explosives. **0** explosives are allowed. **1** no explosive weapons. **2** no dynamite.
nofalldamage     | 0 - 2             | 0             | Enable/disable fall damage. **0** Fall damage disabled only on `surfaceparm nodamage` **1** Fall damage enabled only on `surfaceparm nodamage` **2** Fall damage disabled everywhere.
noghost          | 0 or 1            | 0             | Disables player ghosting (nonsolid players). Overrides `g_ghostPlayers` server cvar.
nogod            | 0 or 1            | 0             | Disables god mode.
nogoto           | 0 or 1            | 0             | Disables goto.
nojumpdelay      | 0 or 1            | 0             | Enable/disable jump delay. **0** No jump delay only on `surfaceparm monsterslicknorth` **1** Jump delay only on `surfaceparm monsterslicknorth`.
nonoclip         | 0 or 1            | 0             | Enable/disable noclip. **0** Don't allow noclip inside `surfaceparm donotenterlarge` **1** Only allow noclip inside `surfaceparm donotenterlarge`.
nosave           | 0 or 1            | 0             | Enable/disable save. **0** Don't allow save inside `surfaceparm clusterportal` brushes **1** Only allow save inside `surfaceparm clusterportal` brushes.
nooverbounce     | 0 or 1            | 0             | Enable/disable overbounces. **0** Don't allow overbounces on `surfaceparm monsterslicksouth` **1** Only allow overbounces on `surfaceparm monsterslicksouth`.
noprone          | 0 or 1            | 0             | Enable/disable prone. **0** Don't allow prone inside `surfaceparm donotenter` brushes **1** Only allow prone inside `surfaceparm donotenter` brushes.
nowallbug        | 0 or 1            | 0             | Toggles whether players can accelerate while stuck in a wall.
portalgun_spawn  | 0 or 1            | 0             | Toggles whether players should spawn with a portal gun.
portalsurfaces   | 0 or 1            | 1             | Enable/disable portalsurfaces. **0** Only allow portals on `surfaceparm monsterslickeast` **1** Don't allow portals on `surfaceparm monsterslickeast`.
portalteam       | 0 - 2             | 0             | If set to **0**, players can only go to own portals. If set to **1**, players can also go to fireteam mates' portals. If set to **2**, anyone can go to anyones portals.
limitedsaves     | any integer       | 0             | If set to higher than 0, saves are limited to the set value.
strictsaveload   | bitflag or string | 0             | Limits save and load by given conditions. **1/move** cannot save while moving **2/dead** cannot save/load while dead. Combine strings with `|` (eg. `move | dead`).

**Spawnflags:**
_None_

---

## Deprecated entities

These entities are considered deprecated, and while still functional, usage is discouraged.

---

## target_activate

### Reason for deprecation
Replaced by [target and trigger_tracker](#target_tracker-and-trigger_tracker)

---

Activates targeted entities if ident requirement is set.

**Keys**

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
reqident         | any integer       | 0             | Ident value required for activation.

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
1          | Fires targets if activators ident value is greater than `reqident`
2          | Fires targets if activators ident value is not `reqident`
4          | Fires targets if activators ident value is less than `reqident`

_Note: By default triggers if ident is equal. Fires a random target instead of all targets._

---

## target_decay

### Reason for deprecation
Replaced by [target and trigger_tracker](#target_tracker-and-trigger_tracker)

---

Decays activators ident value.

**Keys**

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
ident            | any integer       | -1            | Ident value required for activation.
decay_time       | any integer       | -1            | How long in milliseconds it takes for ident to decay to specified value.
decay_value      | any integer       | -1            | Value to which ident decays to.

**Spawnflags:**
_None_

---

## target_increase_ident

### Reason for deprecation
Replaced by [target and trigger_tracker](#target_tracker-and-trigger_tracker)

---

Increases the players map progression identifier.

**Keys**`trigger_multiple`

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
inc              | any integer       | 1             | How much the identifier should be increased when player activates the entity.

**Spawnflags:**
_None_

---

## target_printname

### Reason for deprecation
[target_print](#target_print) provides all the same functionality as this entity.

---

Prints `message` as a popup message. If no spawnflags are specified, prints to all clients, including spectators.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
message          | any string        |               | Message to print. `%s` can be used to print the activators name.

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
1          | Only print for Axis.
2          | Only print for Allies.
4          | Only print for the activator.

---

## target_setident

### Reason for deprecation
Replaced by [target and trigger_tracker](#target_tracker-and-trigger_tracker)

---

Sets the activator's map progression identifier.

**Keys**

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
ident            | any integer       | 0             | The value the identifier will be set to.

**Spawnflags:**
_None_

---

## trigger_multiple

### Reason for deprecation
Since ETJump 3.1.0, the `spawnflags 2048` behavior was made default. `spawnflags 512` has been deprecated as all it did was essentially set `wait` to `1000 / sv_fps`.

---

Activates targets when touched.

**Keys:**
_None_

**Spawnflags**

Spawnflag  | Description
:---------:|:-----------
512        | Activates every server frame.
2048       | Acitavtes for all touching clients with unique wait cycles.
