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
Loads a backup slot. Possible slots __1__-__3__. If no slot is given, loads slot __1__.

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
Changes to class with weapon. Possible classes are __s__, __e__, __m__, __f__, __c__. Possible weapons are __1__-__7__.

---

## clearsaves
`clearsaves`  
Clears users saved positions in all slots.

_Note: Removes saved slots on both teams._

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

## listinfo
`listinfo [map list]`  
Lists all callvote randommap map lists. If a map is given, lists the maps on the list.

---

## listspawnpt
`listspawnpt`  
Lists all valid spawnpoints in the map. The value in __[brackets]__ indicates the spawnpoint number (used with `setspawnpt`) and the letters __A__ and __X__ indicate if the spawnpoint belongs to Allies or Axis, respectively.

---

## load
`load [slot]`  
Loads a previously saved position. Possible slots __0__-__2__. If no slot is given, loads slot __0__.

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

## ob_save, ob_reset
`ob_save`, `ob_reset`  
Saves/resets current coordinates for overbounce watcher.

---

## portal
`portal`  
Prints information about portal gun.

---

## ranks, records, times and top
`ranks [run name]`, `records [run name]`, `times [run name]`, `top [run name]`  
Prints top records in each run on the map. If a run name is given, prints top __50__ records on that run.

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

## save
`save [slot]`  
Saves current position. Possible slots __0__-__2__. If no slot is given, slot is __0__.

---

## setoffset
`setoffset [X Y Z]`  
Offsets your position by the amount of units on each vector. Usage requires access to `noclip`. Maximum offset value per vector is __4096__.

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
Prints your current tracker values on given indices. Special case `all` prints tracker values on every index. If no index is specified, defaults to index __1__.

_Note: Usage of this command requires the server to have `g_debugTrackers 1`. Timerun records are not saved when tracker debugging is enabled._

---

## tracker_set
`tracker_set [index|all] [value]`  
Sets your tracker on given index to specified value. Special case `all` sets specified value in all indices. If no index is specified, defaults to index __1__.

_Note: Usage of this command requires the server to have `g_debugTrackers 1`. Timerun records are not saved when tracker debugging is enabled._

---

## unload
`unload`  
Undo your last `load` command and teleport back to the position you last executed a load from. The position must be a valid position for using `save` (e.g. cannot use `unload` to teleport to an area where you cannot `save`).

_Note: `unload` cannot be used during timeruns. There is only a single slot available, which is overwritten on every successful `load` command._

---
