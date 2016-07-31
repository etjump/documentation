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

## target_increase_ident
Increases the players map progression identifier.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
inc              | any integer       | 1             | How much the identifier should be increased when player activates the entity.

---

## target_printname
Works exactly like `target_print`, but prints the message as popup rather than centerprint. Prints __activator's name__ if message contains `%s`.

---

## target_remove_portals
Removes activators's existing portals.

---

## target_save
Saves current position to activators's save slot 0.

---

## target_savereset
Resets activator's saved positions.

---

## target_scale_velocity
Scales activator's velocity.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
scale            | any integer       | 1             | How many times should be velocity be multiplied.

---

## target_setident
Sets the activator's map progression identifier.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
ident            | any integer       | 0             | The value the identifier will be set to.

---

## target_startTimer
Starts a timerun for activator.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
name             | any text          | default       | The name of the run. Start and stop timer must have a matching name.
spawnflags       | 0, 1, 2, 4        | 0             |  __0__ always reset the run. __1__ reset the run on team change. __2__ reset the run on death. __4__ only reset when you reach the end.

---

## target_stopTimer
Stops a timerun for activator.

Key              | Values            | Default       | Description
-----------------|:-----------------:|---------------|------------
name             | any text          | default       | The name of the run. Start and stop timer must have a matching name.

---

## trigger_tracker and target_tracker
Replacement for target_activate.

There are three different formats for specifying the tracker index and value.

1. __[value]__ Set the tracker on index __1__ to __[value]__
2. __[index,value]__ Set the tracker on index __[index]__ to __[value]__
3. __[index1,value1]|[index2,value2]|..|[indexN,valueN]__ Set the trackers on indices __[index1, index2, .., indexN]__ to values __[value1, value2, .., valueN]__

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
tracker_set_if   | [index,value] format specified above. | 1,-1 | Tracker sets player's tracker value to the specified value if conditions are true.
tracker_inc      | [index,value] format specified above. | 1,0 | Tracker increases player's target value by the specified value.
tracker_inc_if   | [index,value] format specified above. | 1,0 | Tracker increases player's target value by the specified value if conditions are true.

---

## weapon_portalgun
Spawns a portal gun at the location.

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
portalgun_spawn  | 0 or 1            | 0             | Toggles whether players should spawn with a portal gun.
portalsurfaces   | 0 or 1            | 1             | If set to __1__, players can shoot portals everywhere on the map. If set to __0__, players can only shoot portals to areas with `surfaceparm monsterslickeast`.
portalteam       | 0 - 2             | 0             | If set to __0__, players can only go to own portals. If set to __1__, players can also go to fireteam mates' portals. If set to __2__, anyone can go to anyones portals.
savelimit        | any integer       | 0             | If set to higher than 0, saves are limited to the set value.
