# ETJump mapping entities
Here you will find full list of ETJump entities you can use in your map. Included on this list are also stock ET entities that have been expanded or fixed by ETJump.

## etjump203_target_relay
A `target_relay` that works only on __ETJump 2.0.3__ and newer.

_Note: Fires a random target instead of all targets._

---

## etjump2_target_relay
A `target_relay` that works only on __ETJump 2.0.0__ and newer.

_Note: Fires a random target instead of all targets._

---

## func_invisible_user
Uses targeted entities on activation.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
noise            | path to .wav      |               | Sound to play on activation.
volume           | any integer       | 255           | Volume of activation sound.

---

## target_activate_if_velocity
Activates targeted entities if player's velocity is between the lower and upper velocity limit.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
lower_limit      | any integer       | 0             | If value is higher than lower limit, targets will be __activated__.
upper_limit      | any integer       | 0             | If value is lower than upper limit, targets will be __activated__.
spawnflags       | 0, 1, 2           | 0             | __1__ only calculate __horizontal__ velocity. __2__ only calculate __vertical__ velocity.

_Note: Fires a random target instead of all targets._

---

## target_give
Gives activator targeted items. Must target actual entites in the map. Standard class restrictions apply when giving weapons (eg. cannot give `weapon_panzerfaust` to a medic).

---

## target_ftrelay
Works like `target_relay` but activates the entities for everyone in the player's current fireteam, not just the player.

_Note: Fires a random target instead of all targets. The target is randomly picked for each fireteam member._

---

## target_interrupt_timerun
Stops any active timerun without setting a record.

---

## target_print
Prints `message` as a centerprint. If no spawnflags are specified, prints to all clients, including spectators.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
spawnflags       | 8                 | 0             | __8__ Prints to CPM (popup messages) instead of centerprint.

---

## target_printname
Prints `message` as a popup message. If no spawnflags are specified, prints to all clients, including spectators.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
message          | any string        |               | Message to print. `%i` and `%s` can be used to print the activators name.
spawnflags       | 0, 1, 2, 4        | 0             | __1__ Only prints for Axis. __2__ Only prints for Allies. __4__ Only prints for activator.

---

## target_push
Pushes activator towards `target` or `angle(s)`.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
spawnflags       | 2, 4              | 0             | __2__ Speed from the pusher is added to activators horizontal speed. __4__ Speed from the pusher is added to activators vertical speed.

---

## target_relay
Fires its targets when activated.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
spawnflags       | 8, 16             | 0             | __8__ Only activates during timerun. __16__ Doesn't activate during timerun.

---

## target_remove_portals
Removes activators existing portals.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
spawnflags       | 0, 1              | 0             | __1__ does not print text when portals are removed.

---

## target_save
Saves current position to activators save slot __0__.

---

## target_savereset and trigger_savereset
Resets activators saved positions.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
spawnflags       | 0, 1              | 0             | __1__ does not print text when saves are reset.

---

## target_scale_velocity
Scales activator's velocity.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
scale            | any integer       | 1             | How many times should be velocity be multiplied.
time             | any integer       | 0             | Time in seconds for constant speed scale when `spawnflags 1` is used.
spawnflags       | 0, 1              | 0             | __1__ Scales base movement speed by `scale` for duration of `time`.

---

## target_set_health
Sets activators health to specified value.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
health           | integer > 0       | 100           | Value to set health to.
wait             | any integer       | 1000          | How long in milliseconds before next activation by same player.
spawnflags       | 0, 1              | 0             | __1__ Only activates for player once per life.

---

## target_startTimer
Starts a timerun for activator.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
name             | any text          | default       | The name of the run. Start and stop timer must have a matching name. Names are case sensitive.
speed_limit      | any integer       | 700           | Timerun does not start if player has higher starting speed than specified.
spawnflags       | 0, 1, 2, 4, 8, 16, 32, 64, 128 | 0 |  __0__ always reset the run. __1__ reset the run on team change. __2__ reset the run on death. __4__ only reset when you reach the end. __8__ run resets if client sets `pmove_fixed 0`. __16__ disables `backup` and extra save slots. __32__ cannot pickup explosive weapons. __64__ cannot pickup portalgun. __128__ Disables `save`, `load` resets run.

Starting a timerun performs the following actions to the activating player:

* Removes explosive weapons and flamethrower
* Removes all projectiles and mines of the activator
* Removes portalgun
* Resets portals
* Clears all save slots and backups (unless `spawnflags 128` is used)

---

## target_stopTimer
Stops a timerun for activator.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
name             | any text          | default       | The name of the run. Start and stop timer must have a matching name. Names are case sensitive.

---

---

## target_teleporter and trigger_teleport
Teleports player to target location.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
outspeed         | any integer       | 0             | Fixed speed at which player exits at target destination. __0__ to ignore.
noise            | path to .wav      |               | Sound to play on activation.
spawnflags       | 0, 1, 2, 4, 8, 16 | 0             | __1__ Reset activators speed. __2__ Convert activators speed towards angle of destination. __4__ Convert angle and speed relative to destination while preserving yaw. __8__ Convert angle and speed relative to destination while preserving yaw and pitch. __16__ Apply __160ms__ long knockback event after teleportation (Q3 behavior).

---

## target_tracker and trigger_tracker
Replacement for target_activate.

There are three different formats for specifying the tracker index and value.

1. __[value]__ Set the tracker on index __1__ to __[value]__
2. __[index,value]__ Set the tracker on index __[index]__ to __[value]__
3. __[index1,value1]|[index2,value2]|..|[indexN,valueN]__ Set the trackers on indices __[index1, index2, .., indexN]__ to values __[value1, value2, .., valueN]__

Valid range for tracker indices is __1-50__.

__Examples__

Key              | Values            | Meaning
-----------------|:-----------------:|----------
tracker_eq       | 1                 | tracker on index 1 has to be 1
tracker_eq       | 2,1               | tracker on index 2 has to be 1
tracker_eq       | 1,1&#124;2,1&#124;3,1 | trackers on indices 1, 2 and 3 have to be 1

__Keys__

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
tracker_eq       | [index,value] format specified above. | 1,-1 | Tracker activates targets if specified tracker value matches the player's tracker value.
tracker_not_eq   | [index,value] format specified above. | 1,-1 | Tracker activates targets if specified tracker value does not match the player's tracker value.
tracker_gt       | [index,value] format specified above. | 1,-1 | Tracker activates targets if player's tracker value is greater than specified value.
tracker_lt       | [index,value] format specified above. | 1,-1 | Tracker activates targets if player's tracker value is less than the specified value.
tracker_set      | [index,value] format specified above. | 1,-1 | Tracker sets player's tracker value to the specified value.
tracker_set_if   | [index,value] format specified above. | 1,-1 | Tracker sets player's tracker value to the specified value if conditions from `tracker_eq`, `tracker_not_eq`, `tracker_gt` or `tracker_lt` are met.
tracker_inc      | [index,value] format specified above. | 1,0 | Tracker increases player's tracker value by the specified value.
tracker_inc_if   | [index,value] format specified above. | 1,0 | Tracker increases player's tracker value by the specified value if conditions from `tracker_eq`, `tracker_not_eq`, `tracker_gt` or `tracker_lt` are met.

---

## trigger_multiple
Activates targets when touched.

Key              | Values            | Default       | Description
-----------------|:-----------------:|:-------------:|------------
spawnflags       | 512, 2048         | 0             | __512__ activates every server frame. __2048__ activates for every touching client with unique wait times.

---

## trigger_push
Pushes activator towards `target` or `angle(s)`. This entity is client side predicted.

Key              | Values            | Default       | Description
-----------------|:-----------------:|:-------------:|------------
speed            | any integer       | 1000          | Speed at which player is launched. No effect if targeting an entity.
noise            | path to .wav      |               | Sound to play on activation.
spawnflags       | 0, 2, 4           | 0             | __2__ Speed from the pusher is added to activators horizontal speed. __4__ Speed from the pusher is added to activators vertical speed.

---

## weapon_portalgun
Spawns a portal gun at the location.

Key              | Values            | Default       | Description
-----------------|:-----------------:|:-------------:|------------
spawnflags       | 0, 2, 4           | 0             | __2__ spins around its axis. __4__ bobs up and down.

---

## Worldspawn keys

Key              | Values            | Default       | Description
-----------------|:-----------------:|:-------------:|------------
noexplosives     | 0 - 2             | 0             | Disables explosives. __0__ explosives are allowed. __1__ no explosive weapons. __2__ no dynamite.
nofalldamage     | 0 - 2             | 0             | Enable/disable fall damage. __0__ Fall damage disabled only on `surfaceparm nodamage` __1__ Fall damage enabled only on `surfaceparm nodamage` __2__ Fall damage disabled everywhere.
noghost          | 0 or 1            | 0             | Disables player ghosting (nonsolid players). Overrides `g_ghostPlayers` server cvar.
nogod            | 0 or 1            | 0             | Disables god mode.
nogoto           | 0 or 1            | 0             | Disables goto.
nojumpdelay      | 0 or 1            | 0             | Enable/disable jump delay. __0__ No jump delay only on `surfaceparm monsterslicknorth` __1__ Jump delay only on `surfaceparm monsterslicknorth`.
nonoclip         | 0 or 1            | 0             | Disables noclip.
nosave           | 0 or 1            | 0             | Enable/disable save. __0__ Don't allow save inside `surfaceparm clusterportal`brushes __1__ Only allow save inside `surfaceparm clusterportal` brushes.
nooverbounce     | 0 or 1            | 0             | Enable/disable overbounces. __0__ Don't allow overbounces on `surfaceparm monsterslicksouth` __1__ Only allow overbounces on `surfaceparm monsterslicksouth`.
noprone          | 0 or 1            | 0             | Enable/disable prone. __0__ Don't allow prone inside `surfaceparm donotenter`brushes __1__ Only allow prone inside `surfaceparm donotenter` brushes.
portalgun_spawn  | 0 or 1            | 0             | Toggles whether players should spawn with a portal gun.
portalsurfaces   | 0 or 1            | 1             | Enable/disable portalsurfaces. __0__ Only allow portals on `surfaceparm monsterslickeast` __1__ Don't allow portals on `surfaceparm monsterslickeast`.
portalteam       | 0 - 2             | 0             | If set to __0__, players can only go to own portals. If set to __1__, players can also go to fireteam mates' portals. If set to __2__, anyone can go to anyones portals.
savelimit        | any integer       | 0             | If set to higher than 0, saves are limited to the set value.
strictsaveload   | bitmask or string | 0             | Limits save and load by given conditions. __1/move__ cannot save while moving __2/dead__ cannot save/load while dead. Combine strings with `|` (eg. `move | dead`).

---

# Legacy ident system
The ident system was initially created to track map progression. While still functional, it has been deprecated in favor of tracker system (`trigger_tracker` and `target_tracker`). It's not recommended to use these entities when creating new maps, and there won't be new entities to expand the system.


## target_activate
Activates targeted entities if ident requirement is set.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
reqident         | any integer       | 0             | Ident value required for activation.
spawnflags       | 0, 1, 2, 4        | 0             | __0__ trigger if equal. __1__ trigger if greater. __2__ trigger if not. __4__ trigger if lower.

_Note: Fires a random target instead of all targets._

---

## target_decay
Decays activators ident value.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
ident            | any integer       | -1            | Ident value required for activation.
decay_time       | any integer       | -1            | How long in milliseconds it takes for ident to decay to specified value.
decay_value      | any integer       | -1            | Value to which ident decays to.

---

## target_increase_ident
Increases the players map progression identifier.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
inc              | any integer       | 1             | How much the identifier should be increased when player activates the entity.

---

## target_setident
Sets the activator's map progression identifier.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
ident            | any integer       | 0             | The value the identifier will be set to.
