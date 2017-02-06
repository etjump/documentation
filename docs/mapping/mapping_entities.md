# ETJump mapping entities
Here you will find full list of ETJump entities you can use in your map.

## etjump203_target_relay
A `target_relay` that works only on __ETJump 2.0.3__ and newer.

---

## etjump2_target_relay
A `target_relay` that works only on __ETJump 2.0.0__ and newer.

---

## target_activate_if_velocity
Activates targeted entities if player's velocity is between the lower and upper velocity limit.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
spawnflags       | 0, 1, 2           | 0             |  If __0__, speed will be calculated from __horizontal and vertical__ velocity. If __1__, speed will be calculated from __horizontal__ velocity. If __2__, speed will be calculated from __vertical__ velocity.
lower_limit      | any integer       | 0             | If value is higher than lower limit, targets will be __activated__.
upper_limit      | any integer       | 0             | If value is lower than upper limit, targets will be __activated__.

---

## target_ftrelay
Works exactly like `target_relay` but activates the entities for everyone in the player's current fireteam, not just the player.

---

## target_interrupt_timerun
Stops any active timerun without setting a record.

---

## target_printname
Works exactly like `target_print`, but prints the message as popup rather than centerprint. Prints __activator's name__ if message contains `%s` or `i%`. Supports same spawnflags as `target_print`.

---

## target_remove_portals
Removes activators's existing portals.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
spawnflags       | 0, 1              | 0             | __1__ does not print text when portals are removed.

---

## target_save
Saves current position to activators's save slot 0.

---

## target_savereset and trigger_savereset
Resets activator's saved positions.

---

## target_scale_velocity
Scales activator's velocity.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
scale            | any integer       | 1             | How many times should be velocity be multiplied.

---

## target_set_health
Sets activators health to specified value.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
health           | any integer       | 100           | Value to set health to.
wait             | any integer       | 1000          | How long in milliseconds before next activation by same player.
spawnflags       | 0, 1              | 0             | __1__ Only activates for player once per life.

---

## target_startTimer
Starts a timerun for activator.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
name             | any text          | default       | The name of the run. Start and stop timer must have a matching name. Names are case sensitive.
speed_limit      | any integer       | 700           | Timerun does not start if player has higher starting speed than specified.
spawnflags       | 0, 1, 2, 4, 8, 16, 32, 64        | 0             |  __0__ always reset the run. __1__ reset the run on team change. __2__ reset the run on death. __4__ only reset when you reach the end. __8__ run does not start unless player has `pmove_fixed 1`. __16__ disables `save` and `backup`. __32__ cannot pickup explosive weapons. __64__ cannot pickup portalgun.

---

## target_stopTimer
Stops a timerun for activator.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
name             | any text          | default       | The name of the run. Start and stop timer must have a matching name.

---

## target_tracker and trigger_tracker
Replacement for target_activate.

There are three different formats for specifying the tracker index and value.

1. __[value]__ Set the tracker on index __1__ to __[value]__
2. __[index,value]__ Set the tracker on index __[index]__ to __[value]__
3. __[index1,value1]|[index2,value2]|..|[indexN,valueN]__ Set the trackers on indices __[index1, index2, .., indexN]__ to values __[value1, value2, .., valueN]__

Tracker index has an upper limit of 50.

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
tracker_gt       | [index,value] format specified above. | 1,-1 | Tracker activates targets if player's tracker value is greater than specified value.
tracker_lt       | [index,value] format specified above. | 1,-1 | Tracker activates targets if player's tracker value is less than the specified value.
tracker_set      | [index,value] format specified above. | 1,-1 | Tracker sets player's tracker value to the specified value.
tracker_set_if   | [index,value] format specified above. | 1,-1 | Tracker sets player's tracker value to the specified value if conditions from `tracker_eq`, `tracker_gt` or `tracker_lt` are met.
tracker_inc      | [index,value] format specified above. | 1,0 | Tracker increases player's target value by the specified value.
tracker_inc_if   | [index,value] format specified above. | 1,0 | Tracker increases player's target value by the specified value if conditions from `tracker_eq`, `tracker_gt` or `tracker_lt` are met.

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
noghost          | 0 or 1            | 0             | Disables player ghosting
nogod            | 0 or 1            | 0             | Disables god mode
nogoto           | 0 or 1            | 0             | Disables goto
nonoclip         | 0 or 1            | 0             | Disables noclip
nosave           | 0 or 1            | 0             | Disables save
nooverbounce     | 0 or 1            | 0             | If set to __1__, players can only do overbounces on surfaces with `surfaceparm monsterslicksouth`
portalgun_spawn  | 0 or 1            | 0             | Toggles whether players should spawn with a portal gun.
portalsurfaces   | 0 or 1            | 1             | If set to __1__, players can shoot portals everywhere on the map. If set to __0__, players can only shoot portals to areas with `surfaceparm monsterslickeast`.
portalteam       | 0 - 2             | 0             | If set to __0__, players can only go to own portals. If set to __1__, players can also go to fireteam mates' portals. If set to __2__, anyone can go to anyones portals.
savelimit        | any integer       | 0             | If set to higher than 0, saves are limited to the set value.

---

# Legacy ident system
The ident system was initially created to track map progression. While still functional, it has been deprecated in favor of tracker system (`trigger_tracker` and `target_tracker`). It's not recommended to use these entities when creating new maps, and there won't be new entities to expand the system.


## target_activate
Activates targeted entities if ident requirement is set.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
reqident         | any integer       | 0             | Ident value required for activation.
spawnflags       | 1, 2, 4           | 0             | __0__ trigger if equal. __1__ trigger if greater. __2__ trigger if not. __4__ trigger if lower.

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
