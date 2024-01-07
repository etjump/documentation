# List of ETJump client commands
Below is a list of all available ETJump related console commands for players.

## ad_save
`ad_save [optional name]`  
Saves the current temp demo recorded by autodemo with the given name. The manually saved autodemo naming format is `playername_map_name[DD-MM-YY-HHMMSS]`. If no name is given, defaults to `demo`.

_Note: This only saves the latest temp demo recorded with `etj_autoDemo`. If you are manually recording a demo and use this command, it will take the latest `temp/temp_N.dm_84` and save that. The manually recorded demo will be saved normally into whatever folder you're recording into, with the name it was recorded with._

---

## await
`await [frames] [command1] | [command2] | [command3]...`  
Queues commands to be executed after `[frames]`. Unlike `wait`, this works asynchronously without interrupting other user actions.

_Note: `await` cannot be used during timeruns, and queued commands are cleared when a timerun starts._

---

## backup
`backup [slot]`  
Loads a backup slot. Possible slots **1**-**3**. If no slot is given, loads slot **1**.

---

## call
`call [player]`  
Teleports target player to you.

---

## chs
`chs`  
Prints the list of available CHS infos to console.

---

## class
`class [class] [weapon]`  
Changes to class with weapon. Possible classes are **s**, **e**, **m**, **f**, **c**. Possible weapons are **1**-**7**.

---

## clearsaves
`clearsaves`  
Clears users saved positions in all slots.

_Note: Removes saved slots on both teams._

---

## customvotes, listinfo
`customvotes [list]`  
Lists all callvote custom map vote lists. If `[list]` is given, lists the maps on the specified list.

---

## cv
`cv`  
Alias for `callvote`.

---

## extraTrace
`extraTrace`  
Prints the list of bitmask values for `etj_extraTrace`.

---

## goto
`goto [player]`  
Teleports you to target player.

---

## ignore and unignore
`ignore/unignore [player/ID]`  
Ignores/unignores chat and private messages sent by specified client.

---

## incrementVar
`incrementVar [cvar] [start] [end] [step]`  
Cycles given cvar between values of `start` and `end` with increments of `step`. Same as `cycle`, but supports float values.

---

## interruptRun
`interruptRun`  
Interrupts a currently active timerun.

---

## iwant
`iwant [player]`  
Same as call.

---

## listspawnpt
`listspawnpt`  
Lists all valid spawnpoints in the map. The value in **[brackets]** indicates the spawnpoint number (used with `setspawnpt`) and the letters **A** and **X** indicate if the spawnpoint belongs to Allies or Axis, respectively.

---

## load
`load [slot]`  
Loads a previously saved position. Possible slots **0**-**2**. If no slot is given, loads slot **0**.

---

## loadcheckpoints
`loadcheckpoints [run name]`  
`loadcheckpoints [run name] [rank]`  
Loads timerun checkpoints for comparison for given timerun. If `[rank]` isn't specified, defaults to rank 1 time. Loaded checkpoints can be cleared by specifying `-1` as rank. `[run name]` supports partial matching.

---

## man and manual
`manual [command]`  
Prints a manual for command.

---

## min and minimize
`min`, `minimize`  
Minimizes the ET client. Only works on Windows.

---

## mod_information
`mod_information`  
Prints the ETJump version the server is running.

---

## nocall
`nocall`  
Toggles whether other players are allowed to call you.

---

## nogoto
`nogoto`  
Toggles whether other players can teleport to you.

---

## ob_save, ob_load, ob_reset, ob_list
`ob_save [name]`  
`ob_load [name]`  
`ob_reset`  
`ob_list`  
Manages overbounce watcher coordinates. `ob_save [name]` will save a coordinate with the given name. `ob_load [name]` loads a saved coordinate with given name. `ob_reset` clears all saved positions. `ob_list` displays all saved coordinates.

---

## portal
`portal`  
Prints information about portal gun.

---

## rankings
`rankings [season]`  
`rankings --season [season] --page [page] --page-size [page size]`  
Prints timerun rankings. If no parameters are given, prints top **20** overall rankings.

---

## ranks, records, times and top
`records [run name]`  
`records [map name] [run name]`  
`records [season] [map name] [run name]`  
`records --season [season] --map [map name] --run [run name] --page [page] --page-size [page size]`  
Prints timerun records with given parameters. If `[run name]` isn't specified, prints top **3** records of all timeruns in the map. If specified, will print top **20** records for given run. If `[season]` isn't specifed, prints overall records. `[run name]`, `[map name]` and `[season]` support partial name matching.

_Note: `ranks`, `reconds`, `times` and `top` are all valid aliases for this command._

---

## resetmaxspeed
`resetmaxspeed`  
Resets the maximum speed displayed at speedmeter 1.

---

## resetJumpSpeeds
`resetJumpSpeeds`  
Queues reset for jump speeds display. This command is automatically executed upon death, team change, `save` and `load`. The display will reset on next jump event.

---

## resetStrafeQuality
`resetStrafeQuality`  
Queues reset for strafe quality display. This command is automatically executed upon death, team change, `save` and `load`. The display will reset the next time you're in air or on slick.

---

## resetUpmoveMeter
`resetUpmoveMeter`  
Resets the upmove meter display. This command is automatically executed upon death, team change, `save` and `load`.

---

## rtvVote
`rtvVote [number]`  
Casts a vote for the map specified by `[number]` in an ongoing Rock The Vote.

---

## save
`save [slot]`  
Saves current position. Possible slots **0**-**2**. If no slot is given, slot is **0**.

---

## setoffset
`setoffset [X Y Z]`  
Offsets your position by the amount of units on each vector. Usage requires access to `noclip`. Maximum offset value per vector is **4096**.

---

## specinvite, specuninvite
`specinvite [name/clientnum]`, `specuninvite [name/clientnum]`  
Invites/uninvites specified client to spectate you.

---

## speclist
`speclist`  
Prints a list of clients who are allowed to spectate you while speclocked.

---

## speclock, specunlock
`speclock`, `specunlock`  
Locks/unlocks you from spectators. When locked, use `specinvite/specuninvite` to invite/uninvite clients to spectate you.

---

## tracker_print
`tracker_print [index1|all] [index2] [index3]...`  
Prints your current tracker values on given indices. Special case `all` prints tracker values on every index. If no index is specified, defaults to index **1**.

_Note: Usage of this command requires the server to have `g_debugTrackers 1`. Timerun records are not saved when tracker debugging is enabled._

---

## tracker_set
`tracker_set [index|all] [value]`  
Sets your tracker on given index to specified value. Special case `all` sets specified value in all indices. If no index is specified, defaults to index **1**.

_Note: Usage of this command requires the server to have `g_debugTrackers 1`. Timerun records are not saved when tracker debugging is enabled._

---

## unload
`unload`  
Undo your last `load` command and teleport back to the position you last executed a load from. The position must be a valid position for using `save` (e.g. cannot use `unload` to teleport to an area where you cannot `save`).

_Note: `unload` cannot be used during timeruns. There is only a single slot available, which is overwritten on every successful `load` command._

---
