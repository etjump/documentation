# List of ETJump client commands
Below is a list of all available ETJump related console commands for players.

---

## ad_save
`ad_save [name]`

Saves the current temp demo recorded with [`etj_autoDemo`](etjump_cvars.md/#etj_autodemo) with the given name. The manually saved autodemo naming format is `playername_map_name[DD-MM-YY-HHMMSS]`. If no name is given, defaults to `demo`.

---

## addCustomCommand
`addCustomCommand <name> <command> [page (1-5)] [slot (1-8)]`  
`addCustomCommand -n <name> -c <command> [-p <page (1-5)>] [-s <slot (1-8)>]`  
`addCustomCommand --name <name> --command <command> [--page <page (1-5)>] [--slot <slot (1-8)>]`  

Adds a new custom command to the custom command menu. If `page` is omitted, defaults to first page with a free slot. If `slot` is omitted, defaults to first free slot on given page.

---

## adminChat
`adminChat`

Opens the chat interface with admin chat selected as the message destination.

---

## await
`await <frames> <command1> | [command2] | [command3]...`  

Queues commands to be executed after `<frames>`. Unlike `wait`, this works asynchronously in the background without interrupting other user actions.

```{note}
`await` cannot be used during timeruns, and queued commands are cleared when a timerun starts.
```

---

## backup
`backup [slot]`

Loads a backup slot. Possible slots **1**-**3**. If no slot is given, loads slot **1**.

---

## call, iwant
`call <name|clientnum>`  
`iwant <name|clientnum>`

Teleports targeted player to you.

```{note}
The targeted player must have allowed calling with the [`nocall`](client_commands.md/#nocall) command.
```

---

## chs
`chs`

Prints the list of available CHS info fields to the console.

---

## class
`class <class> [primary] [secondary]`

Changes players class. If `primary` and/or `secondary` is omitted, uses the default weapon(s) for the class.

* Possible classes are **s**, **e**, **m**, **f** and **c**.
* Possible primary weapons are **1**-**7** (class-dependant).
* Possible secondary weapons are single pistol (**1**) or akimbo pistols (**2**).

```{tip}
You can see all the available class/weapon combinations in the console by executing this command without any arguments.
```

---

## clearsaves
`clearsaves`

Clears users saved positions in all slots.

```{caution}
Removes saved slots on both teams.
```

---

## comparecheckpoints
`comparecheckpoints <run name> [rank-1] <rank-2>`  
`comparecheckpoints [-s <season name>] [-m <map name>] -r <run name> [-rk1 <rank>] -rk2 <rank>`  
`comparecheckpoints [--season <season name>] [--map <map name>] --run <run name> [--rank-1 <rank>] --rank-2 <rank>`

Compare checkpoint times between two runs. If `rank-1` is omitted, defaults to rank 1 time.

```{tip}
`<season name>`, `<map name>` and `<run name>` support partial matching.
```

---

## customvotes, listinfo
`customvotes [list]`

Lists all callvote custom map vote lists. If `[list]` is given, lists the maps on the specified list.

---

## cv
`cv <vote command> [arguments]`

Alias for `callvote`.

---

## deleteCustomCommand
`deleteCustomCommand <page (1-5)> [slot (1-8)]`  
`deleteCustomCommand --page <page (1-5)> [--slot <slot (1-8)>]`  

Deletes a custom command from given page & slot. If `slot` is omitted, deletes the last command on the given `page`.

---

## demoQueue
`demoQueue [command]`

Starts an automated demo playback of all demos from a directory specified by [`etj_demoQueueDir`](etjump_cvars.md/#etj_demoqueuedir) cvar.

Available commands:

* `start` - starts the playback.
* `stop` - stops the playback.
  * Due to limitations with communicating with the engine, this must be used to stop the playback, hitting ESC will simply skip to the next demo.
* `restart` - restarts the playback from the beginning.
* `next` - skips to next demo.
* `previous` - go back to previous demo.
* `goto <index>` - skips to a specified demo in the queue.
* `status` - prints information about the current state of the queue.
* `help [command]` - prints usage information, or help text for a given command.

```{note}
Performing a `vid_restart` while the playback is active will break the playback, due to communication limitations with the engine.
```

---

## editCustomCommand
`editCustomCommand <page (1-5)> <slot (1-8)>`  
`editCustomCommand -p <page (1-5)> -s <slot (1-8)> -n <name> -c <command>`  
`editCustomCommand --page <page (1-5)> --slot <slot (1-8)> --name <name> --command <command>`  

Edits a custom command at given page and slot.

---

## enc_say, enc_say_team, enc_say_buddy, enc_say_admin
`enc_say <message>`  
`enc_say_team <message>`  
`enc_say_buddy <message>`  
`enc_say_admin <message>`

Send a quote-printable encoded message to global, team, fireteam or [admin chat](../server/admin_system.md/#admin-chat), respectively.

```{seealso}
[Quoted-printable - Wikipedia](https://en.wikipedia.org/wiki/Quoted-printable)
``` 

---

## extraTrace
`extraTrace`

Prints the list of bitflag values for [`etj_extraTrace`](etjump_cvars.md/#etj_extratrace).

---

## fireteam
`fireteam rules <rule> <value>`  
`fireteam tj|teamjump <on|1> <off|0>`  
`fireteam countdown [seconds (1-10)]`  

Executes fireteam actions. `rules` and `teamjump` can only be set by the fireteam admin.

Enabling teamjump mode is required for [`target_ftrelay`](../mapping/mapping_entities.md/#target_ftrelay) to activate targets for each fireteam member.

`countdown` will perform an automated countdown in fireteam chat from the given `seconds` value. This can be used to coordinate timings on teamjumps. If `seconds` is not given, the default value will be taken from [`etj_fireteamCountdownLength`](./etjump_cvars.md/#etj_fireteamcountdownlength) cvar.

Available rules:
* `noghost <on|1> <off|0>` - toggles player collision between fireteam members
* `savelimit <limit (-1 - 100|reset)>` - sets savelimit for fireteam members. `-1` means no limit. `reset` restores all the available saves for each member.

---

## generateCustomCommandsFile
`generateCustomCommandsFile [-f]`  
`generateCustomCommandsFile [--force]`

Generates an example file for [custom command menu](../basic_features.md/#custom-command-menu). If the file exists, `--force` must be used to overwrite the existing file.

```{note}
The example file will always be generated using the default filename (`custom_commands.dat`), regardless of [`etj_ccMenu_filename`](etjump_cvars.md/#etj_ccmenu_filename) cvar value.
```

## goto
`goto <name|clientnum>`

Teleports you to the target player.

```{note}
The targeted player must have allowed goto with the [`nogoto`](./client_commands.md/#nogoto) command.
```

---

## help, man, manual
`help [command]`  
`man [command]`  
`manual [command]`

Prints a manual for command. If command isn't specifiec, prints help for the command itself.

```{note}
Not all commands have a help page configured - this will be improved in the future.
```

---

## ignore and unignore
`ignore/unignore <name|clientnum>`

Ignores/unignores chat and private messages sent by specified client.

```{note}
Ignore lasts for the duration of your session. Once you disconnect from the server, the ignored clients are cleared.
```

---

## incrementVar
`incrementVar <cvar> <start> <end> [step]`

Cycles given cvar between values of `start` and `end` with increments of `step`. If `step` isn't given, toggles between `start` and `end`.

```{hint}
This functions the same way as `cycle`, but supports floating point values.
```

---

## interruptRun
`interruptRun`

Interrupts your currently active timerun.

---

## listcheckpoints
`listcheckpoints <run name> [rank]`  
`listcheckpoints <map name> <run name> <rank>`  
`listcheckpoints <season name> <map name> <run name> <rank>`  
`listcheckpoints [-s <season name>] [-m <map name>] -r <run name> [-rk <rank>]`  
`listcheckpoints [--season <season name>] [--map <map name>] --run <run name> [--rank <rank>]`  

Lists checkpoint times from the given run. If `rank` is omitted, defaults to **1**.

```{tip}
`<season name>`, `<map name>` and `<run name>` support partial matching.
```

---

## listCustomCommands
`listCustomCommands [page (1-5)]`

Lists saved custom commands in the currently loaded custom command file. If `page` is given, lists only commands from that page.

---

## listsavepos
`listsavepos`

Lists all valid savepos files in `etjump/savepos` directory.

```{hint}
If manually adding a savepos file to the directory while the game is running, make sure to reload the files using [`readsavepos`](client_commands.md/#readsavepos).
```

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
`loadcheckpoints <run name> [rank]`  
`loadcheckpoints -r <run name> [-rk <rank>]`  
`loadcheckpoints --run <run name> [--rank <rank>]`

Loads timerun checkpoints for comparison for given timerun. If `[rank]` isn't specified, defaults to rank 1 time. Loaded checkpoints can be cleared by specifying `-1` as rank.

```{tip}
`<run name>` supports partial name matching, the exact run name isn't required.
```

---

## loadpos
`loadpos [name]`

Loads a given savepos file. If `[name]` isn't given, defaults to `default`.

```{note}
Cheats must be enabled in order to use this command.
```

```{seealso}
[`savepos`](#savepos)
```

---

## ma, say_admin
`ma <message>`  
`say_admin <message>`

Sends a message to [admin chat](../server/admin_system.md/#admin-chat).

---

## min, minimize
`min`  
`minimize`

Minimizes the ET client. Only works on Windows.

---

## mod_information
`mod_information`

Prints the ETJump version the server is running.

---

## moveCustomCommand
`moveCustomCommand <from-page (1-5)> <from-slot (1-8)> <to-page (1-5)> [to-slot (1-8)]`  
`moveCustomCommand -fp <page (1-5)> -fs <slot (1-8)> -tp <page (1-5)> [-ts <slot (1-8)>]`  
`moveCustomCommand --from-page <page (1-5)> --from-slot <slot (1-8)> --to-page <page (1-5)> [--to-slot <slot (1-8)>]`  

Moves a command from the give slot/page to another page/slot. If `to-slot` is omitted, defaults to first free slot on the given page. If `to-slot` on the targeted page already has a command in it, the commands will be swapped.

```{note}
Swapping commands only happens if `--to-slot` argument is explicitly given. If the targeted page is full, the move fails, unless the target slot is specified (which will swap the commands between from/to pages/slots).
```

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

Manages overbounce watcher coordinates. `ob_save [name]` will save a coordinate with the given name. `ob_load [name]` loads a saved coordinate with given name. `ob_reset` clears all saved positions. `ob_list` displays all saved coordinates. If `[name]` isn't given, defaults to `default`.

---

## openCustomCommandMenu
`openCustomCommandMenu [page (1-5)]`

Toggles the custom command menu. If `page` is given, opens directly to the specified page.

---

## portal
`portal`

Prints information about the portal gun.

---

## printDemoCompatInfo
`printDemoCompatInfo`

Prints currently active compatibility settings during demo playback.

---

## printMapCustomizationInfo
`printMapCustomizationInfo`

Prints the SHA-1 hashes of custom mapscript and/or custom entity file, currently running on the server.

```{note}
The hashes are calculated with `LF` line endings. If you are comparing the hashes to files you have locally, make sure they are saved with `LF` line endings as well.
```

```{tip}
This can be used during demo playback (starting with demos recorded in ETJump 3.5.0) to display the hashes of the files that were loaded on the server, when the demo was recorded.
```

---

## rankings
`rankings [season]`  
`rankings [-s <season>] [-p <page>] [-ps <page size>]`  
`rankings [--season <season>] [--page <page>] [--page-size <page size>]`

Prints timerun rankings. If no parameters are given, prints top **20** overall rankings.

---

## ranks, records, times, top
`records [run name]`  
`records <map name> <run name>`  
`records <season> <map name> <run name>`  
`records [-s <season>] [-m <map name>] [-r <run name>] [-p <page>] [-ps <page size>]`  
`records [--season <season>] [--map <map name>] [--run <run name>] [--page <page>] [--page-size <page size>]`

Prints timerun records with given parameters. If no arguments are given, prints top **3** records for each run in the current map. If `[run name]` is given, prints top **20** records for the given run. If `[season]` isn't specifed, prints overall records.

```{tip}
`<run name>`, `<map name>` and `<season>` support partial name matching.
```

```{note}
`ranks`, `reconds`, `times` and `top` are all valid aliases for this command.
```

---

## readCustomCommands
`readCustomCommands`

Parses custom command menu from the file pointed to by [`etj_ccMenu_filename`](etjump_cvars.md/#etj_ccmenu_filename). You must execute this command to reload changes to the menu when editing the file by hand, outside the game.

---

## readsavepos
`readsavepos`

Reloads all savepos files in `etjump/savepos` directory.

---

## resetmaxspeed
`resetmaxspeed`

Resets the maximum speed displayed at speedmeter 1.

---

## resetJumpSpeeds
`resetJumpSpeeds`

Queues reset for jump speeds display. This command is automatically executed upon death, team change, [`save`](client_commands.md/#save) and [`load`](client_commands.md/#load). The display will reset on next jump event.

---

## resetStrafeQuality
`resetStrafeQuality`

Queues reset for strafe quality display. This command is automatically executed upon death, team change, [`save`](client_commands.md/#save) and [`load`](client_commands.md/#load). The display will reset the next time you're in air or on slick.

---

## resetUpmoveMeter
`resetUpmoveMeter`

Resets the upmove meter display. This command is automatically executed upon death, team change, [`save`](client_commands.md/#save) and [`load`](client_commands.md/#load).

---

## rtvVote
`rtvVote <number>`

Casts a vote for the map specified by `<number>` in an ongoing Rock The Vote.

---

## save
`save [slot]`

Saves current position. Possible slots **0**-**2**. If no slot is given, slot is **0**.

---

## savepos
`savepos [name] [flags (0-3)]`

Saves your current position, angles, velocity, stance and timerun state to a savepos file. If `[name]` isn't set, defaults to `default`. If only one argument is given, and the argument is a single number, it is treated as a flag. `[flags]` is a bitflag value with the following options.

* **1** reset velocity to 0
* **2** reset pitch angle to 0

```{hint}
The positions are saved into `etjump/savepos/name.dat`.
```

This works fully client-sided, meaning it's possible to use this command while playing back a demo.

```{note}
Timerun state can only be saved from demos recorded in ETJump 3.3.0 or newer. For demos recorded prior to that, the position will save normally, but loading it won't restore the timerun state.
```

```{seealso}
[`loadpos`](client_commands.md/#loadpos)
```

---

## setoffset
`setoffset <x> <y> <z>`

Offsets your position by the amount of units on each vector. Usage requires access to `noclip`.

```{note}
Maximum offset range per vector is **-4096-4096**.
```

---

## specinvite, specuninvite
`specinvite <name/clientnum>`  
`specuninvite <name/clientnum>`

Invites/uninvites specified client to spectate you.

---

## speclist
`speclist`

Prints a list of clients who are allowed to spectate you while speclocked.

---

## speclock, specunlock
`speclock`  
`specunlock`

Locks/unlocks you from spectators. When locked, use `specinvite/specuninvite` to invite/uninvite clients to spectate you.

---

## toggleETJumpSettings
`toggleETJumpSettings`

Toggles the ETJump settings menu.

```{hint}
This is simply a shortcut to open `ETJump -> Settings -> General/Gameplay` page. The sole purpose of this command is to be able to bind the settings menu toggle to a key.
```

---

## tracker_print
`tracker_print [index1|all] [index2] [index3]...`

Prints your current tracker values on given indices. Special case `all` prints tracker values on every index. If no index is specified, defaults to index **1**.

```{note}
Usage of this command requires the server to have [`g_debugTrackers 1`](../server/server_cvars.md/#g_debugtrackers). Timerun records are not saved when tracker debugging is enabled.
```

---

## tracker_set
`tracker_set [index|all] <value>`

Sets your tracker on given index to specified value. Special case `all` sets specified value in all indices. If no index is specified, defaults to index **1**.

```{note}
Usage of this command requires the server to have [`g_debugTrackers 1`](../server/server_cvars.md/#g_debugtrackers). Timerun records are not saved when tracker debugging is enabled.
```

---

## unload
`unload`

Undo your last [`load`](client_commands.md/#load) command and teleport back to the position you last executed a load from. The position must be a valid position for using [`save`](client_commands.md/#save) (e.g. cannot use `unload` to teleport to an area where you cannot `save`).


```{note}
`unload` cannot be used during timeruns. There is only a single slot available, which is overwritten on every successful `load` command.
```
