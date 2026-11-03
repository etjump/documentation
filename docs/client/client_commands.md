# List of ETJump client commands
Below is a list of all available ETJump related console commands for players.

---

## ad_save
Saves the current temp demo recorded with [`etj_autoDemo`](etjump_cvars.md/#etj_autodemo) with the given name.

`ad_save [name]`

{.option-table}
Option                    | Description
:-------------------------|:------------
name                      | Name of the demo. Defaults to `demo`.

The manually saved autodemo naming format is `playername_map_name[DD-MM-YY-HHMMSS]`.

---

## addCustomCommand
Adds a new custom command to the custom command menu.

`addCustomCommand <command> [name] [page (1-5)] [slot (1-8)]`

{.option-table}
Option                    | Description
:-------------------------|:------------
**-c, --command**         | The command to add.
-n, --name                | Name of the command, default is the command being added.
-p, --page                | The page to add the command to (1-5). Default is the first page with a free slot.
-s, --slot                | The slot to save the command to (1-8). Default is the first free slot on the selected page.

---

## adminChat
Opens the chat interface with admin chat selected as the message destination.

---

## await
Queues commands to be executed after `<frames>`. Unlike `wait`, this works asynchronously in the background without interrupting other user actions. Use the pipe character `|` as a separator if specifying multiple commands to execute.

`await <frames> <command> | [command2] | [command3] | ...`

{.option-table}
Option                    | Description
:-------------------------|:------------
**frames**                | Number of frames to wait before executing the commands.
**command**               | The command to execute.

```{note}
`await` cannot be used during timeruns, and queued commands are cleared when a timerun starts.
```

---

## backup
Loads a backup slot.

`backup [slot]`

{.option-table}
Option                    | Description
:-------------------------|:------------
slot                      | The backup slot to load (1-3). Defaults to **1**.

---

## best-segments
Prints best segments from a timerun.

`best-segments <run name>`  
`best-segments <map name> <run name>`  
`best-segments <season name> <map name> <run name>`

{.option-table}
Option                    | Description
:-------------------------|:------------
**-r, --run**             | Name of the run.
-s, --season              | Name of the season.
-m, --map                 | Name of the map. Default is the current map.
-u, --user                | User ID of the user to print segments for. Default is your own user. Ignored if `-g` is given.
-g, --global              | Prints the overall best times instead of your personal best times.

---

## best-segments-history
Prints the history of a single best segment.

`best-segments-history <run name> <segment>`  
`best-segments-history <map name> <run name> <segment>`  
`best-segments-history <season name> <map name> <run name> <segment>`

{.option-table}
Option                    | Description
:-------------------------|:------------
-s, --season              | Season to print the history from. A partial match prints every matching season. Default is the overall season.
-m, --map                 | Map to print the history from. Default is the current map.
**-r, --run**             | Run to print the history from.
**-sg, --segment**        | The segment to print the history from.
-u, --user                | User ID to print the history for. Default is your own user ID.
-p, --page                | Page of segments history to print.
-ps, --page-size          | How many entries to show on. Defaults to **20**, max is **100**.

```{note}
Historical progression for timerun segments is not recorded for any run prior to ETJump 3.7.0.
```

---

## call, iwant
Teleports targeted player to you.

`call <name|clientnum>`  
`iwant <name|clientnum>`

{.option-table}
Option                    | Description
:-------------------------|:------------
**name\|clientnum**       | The targeted player, specified by name or client number.

```{note}
The targeted player must have allowed calling with the [`nocall`](client_commands.md/#nocall) command.
```

---

## chs
Prints the list of available CHS info fields to the console.

---

## class
Changes players class.

`class <class> [primary] [secondary]`

{.option-table}
Option                    | Description
:-------------------------|:------------
**class**                 | The class to change to. Possible values are **s**, **e**, **m**, **f** and **c**.
primary                   | Primary weapon (1-7, class-dependant). Default is the default weapon for the selected class.
secondary                 | Secondary weapon: single pistol (**1**) or akimbo pistols (**2**). Default is **1**.

```{tip}
You can see all the available class/weapon combinations in the console by executing this command without any arguments.
```

---

## clearsaves
Clears users saved positions in all slots.

```{caution}
Removes saved slots on both teams.
```

---

## comparecheckpoints
Compare checkpoint times between two runs.

`comparecheckpoints <run name> [rank-1] <rank-2>`

{.option-table}
Option                    | Description
:-------------------------|:------------
-s, --season              | Name of the season.
-m, --map                 | Name of the map.
**-r, --run**             | Name of the run.
-rk1, --rank-1            | The first rank to compare. Defaults to **1**.
**-rk2, --rank-2**        | The second rank to compare.

```{tip}
`<season name>`, `<map name>` and `<run name>` support partial matching.
```

---

## customvotes, listinfo
Lists all callvote custom map vote lists.

`customvotes [list]`

{.option-table}
Option                    | Description
:-------------------------|:------------
list                      | If given, lists the maps on the specified list.

---

## cv
Alias for `callvote`.

`cv <vote command> [arguments]`

{.option-table}
Option                    | Description
:-------------------------|:------------
**vote command**          | The vote command to execute.
arguments                 | Arguments passed to the vote command.

---

## deleteCustomCommand
Deletes a custom command from given page & slot.

`deleteCustomCommand <page (1-5)> [slot (1-8)]`

{.option-table}
Option                    | Description
:-------------------------|:------------
**-p, --page**            | The page to delete the command from (1-5).
-s, --slot                | The slot to delete the command from (1-8). Defaults to the last command on the given page.

---

## demoQueue
Starts an automated demo playback of all demos from a directory specified by [`etj_demoQueueDir`](etjump_cvars.md/#etj_demoqueuedir) cvar.

`demoQueue [command]`

{.option-table}
Option                    | Description
:-------------------------|:------------
start                     | Starts the playback.
stop                      | Stops the playback. Due to limitations with communicating with the engine, this must be used to stop the playback, hitting ESC will simply skip to the next demo.
restart                   | Restarts the playback from the beginning.
next                      | Skips to the next demo.
previous                  | Goes back to the previous demo.
goto                      | Skips to the specified demo index in the queue.
status                    | Prints information about the current state of the queue.
help                      | Prints usage information, or help text for a given command.

```{note}
Performing a `vid_restart` while the playback is active will break the playback, due to communication limitations with the engine.
```

---

## editCustomCommand
Edits a custom command at given page and slot.

`editCustomCommand <page (1-5)> <slot (1-8)>`

{.option-table}
Option                    | Description
:-------------------------|:------------
**-p, --page**            | The page the command is on (1-5).
**-s, --slot**            | The slot the command is on (1-8).
-n, --name                | New name for the command.
-c, --command             | New command.

---

## enc_say, enc_say_team, enc_say_buddy, enc_say_admin
Send a quote-printable encoded message to global, team, fireteam or [admin chat](../server/admin_system.md/#admin-chat), respectively.

`enc_say <message>`  
`enc_say_team <message>`  
`enc_say_buddy <message>`  
`enc_say_admin <message>`

{.option-table}
Option                    | Description
:-------------------------|:------------
**message**               | The message to send.

```{seealso}
[Quoted-printable - Wikipedia](https://en.wikipedia.org/wiki/Quoted-printable)
```

---

## extraTrace
Prints the list of bitflag values for [`etj_extraTrace`](etjump_cvars.md/#etj_extratrace).

---

## fireteam
Executes fireteam actions. `rules` and `teamjump` can only be set by the fireteam admin.

`fireteam invite <clientname|clientnum>`  
`fireteam invite <r|b|s>`  
`fireteam invite <axis|allies|allied|spectator|spectators|all>`  
`fireteam rules <rule> <value>`  
`fireteam tj|teamjump <on|1> <off|0>`  
`fireteam countdown [seconds (1-10)]`

{.option-table}
Option                    | Description
:-------------------------|:------------
invite                    | Invites players to the fireteam. Accepts special strings to invite multiple players: either team, all spectators, or all clients on the server.
rules                     | Sets a fireteam rule. Only the fireteam admin can set rules.
tj, teamjump              | Enables or disables teamjump mode. Only the fireteam admin can change this.
countdown                 | Performs an automated countdown in fireteam chat from the given `seconds` value (1-10). Used to coordinate timings on teamjumps. If `seconds` is not given, the default value is taken from [`etj_fireteamCountdownLength`](./etjump_cvars.md/#etj_fireteamcountdownlength) cvar.

Enabling teamjump mode is required for [`target_ftrelay`](../mapping/mapping_entities.md/#target_ftrelay) to activate targets for each fireteam member.

Available rules:
* `noghost <on|1> <off|0>` - toggles player collision between fireteam members
* `savelimit <limit (-1 - 100|reset)>` - sets savelimit for fireteam members. `-1` means no limit. `reset` restores all the available saves for each member.

---

## generateCustomCommandsFile
Generates an example file for [custom command menu](../basic_features.md/#custom-command-menu).

`generateCustomCommandsFile [-f]`

{.option-table}
Option                    | Description
:-------------------------|:------------
-f, --force               | Overwrites the existing file, if it exists.

```{note}
The example file will always be generated using the default filename (`custom_commands.dat`), regardless of [`etj_ccMenu_filename`](etjump_cvars.md/#etj_ccmenu_filename) cvar value.
```

---

## goto
Teleports you to the target player.

`goto <name|clientnum>`

{.option-table}
Option                    | Description
:-------------------------|:------------
**name\|clientnum**       | The targeted player, specified by name or client number.

```{note}
The targeted player must have allowed goto with the [`nogoto`](./client_commands.md/#nogoto) command.
```

---

## help, man, manual
Prints a manual for command.

`help [command]`  
`man [command]`  
`manual [command]`

{.option-table}
Option                    | Description
:-------------------------|:------------
command                   | The command to print a manual for. Defaults to the command itself.

```{note}
Not all commands have a help page configured - this will be improved in the future.
```

---

## ignore and unignore
Ignores/unignores chat and private messages sent by specified client.

`ignore/unignore <name|clientnum>`

{.option-table}
Option                    | Description
:-------------------------|:------------
**name\|clientnum**       | The client to ignore or unignore.

```{note}
Ignore lasts for the duration of your session. Once you disconnect from the server, the ignored clients are cleared.
```

---

## incrementVar
Cycles given cvar between values of `start` and `end` with increments of `step`.

`incrementVar <cvar> <start> <end> [step]`

{.option-table}
Option                    | Description
:-------------------------|:------------
**cvar**                  | The cvar to cycle.
**start**                 | The starting value.
**end**                   | The ending value.
step                      | The increment between values. If not given, toggles between `start` and `end`. Use negative values to decrement the value.

```{hint}
This functions the same way as `cycle`, but supports floating point values.
```

---

## interruptRun
Interrupts your currently active timerun.

---

## listcheckpoints
Lists checkpoint times from the given run.

`listcheckpoints <run name> [rank]`  
`listcheckpoints <map name> <run name> <rank>`  
`listcheckpoints <season name> <map name> <run name> <rank>`

{.option-table}
Option                    | Description
:-------------------------|:------------
-s, --season              | Name of the season.
-m, --map                 | Name of the map.
**-r, --run**             | Name of the run.
-rk, --rank               | Rank to list. Defaults is rank **1**.

```{tip}
`<season name>`, `<map name>` and `<run name>` support partial matching.
```

---

## listCustomCommands
Lists saved custom commands in the currently loaded custom command file.

`listCustomCommands [page (1-5)]`

{.option-table}
Option                    | Description
:-------------------------|:------------
page                      | If given, lists only commands from that page (1-5).

---

## listsavepos
Lists all valid savepos files in `etjump/savepos` directory.

```{hint}
If manually adding a savepos file to the directory while the game is running, make sure to reload the files using [`readsavepos`](client_commands.md/#readsavepos).
```

---

## listspawnpt
Lists all valid spawnpoints in the map. The value in **[brackets]** indicates the spawnpoint number (used with `setspawnpt`) and the letters **A** and **X** indicate if the spawnpoint belongs to Allies or Axis, respectively.

---

## list-removed-records
Lists all records removed with the [`remove-record`](client_commands.md/#remove-record) command. With no filters, prints all removed records.

`list-removed-records <user ID>`  
`list-removed-records <map name> <user ID>`  
`list-removed-records <map name> <run name> <user ID>`  
`list-removed-records <season name> <map name> <run name> <user ID>`

{.option-table}
Option                    | Description
:-------------------------|:------------
-s, --season              | Name of the season.
-m, --map                 | Name of the map.
-r, --run                 | Name of the run.
-u, --user                | ETJump ID of the user whose records to list.
-rb, --removed-by         | ETJump ID of the admin who removed the records.
-p, --page                | Page to display.
-ps, --page-size          | Number of records per page.

---

## list-removed-segments
Lists removed best timerun segments.

`list-removed-segments <user ID>`  
`list-removed-segments <map name> <user ID>`  
`list-removed-segments <map name> <run name> <user ID>`  
`list-removed-segments <season name> <map name> <run name> <user ID>`

{.option-table}
Option                    | Description
:-------------------------|:------------
-s, --season              | Only list removed segments from the given season.
-m, --map                 | Only list removed segments from the given map.
-r, --run                 | Only list removed segments from the given run.
-sg, --segment            | Only list this segment.
-u, --user                | Only list the segments belonging to this user ID.
-rb, --removed-by         | Only list the segments removed by this user ID.
-p, --page                | Which page of removed segments to show.
-ps, --page-size          | How many segments to show per page. Default is **10**, max is **25**.

---

## load
Loads a previously saved position.

`load [slot]`

{.option-table}
Option                    | Description
:-------------------------|:------------
slot                      | The save slot to load (0-2). Defaults to **0**.

---

## loadcheckpoints
Loads timerun checkpoints for comparison for given timerun. Loaded checkpoints can be cleared by specifying `-1` as rank.

`loadcheckpoints <run name> [rank]`

{.option-table}
Option                    | Description
:-------------------------|:------------
**-r, --run**             | Name of the run.
-rk, --rank               | Rank to load. Defaults to **1**. Use `-1` to clear the loaded checkpoints.

```{tip}
`<run name>` supports partial name matching, the exact run name isn't required.
```

---

## loadpos
Loads a given savepos file.

`loadpos [name]`

{.option-table}
Option                    | Description
:-------------------------|:------------
name                      | Name of the savepos file. Defaults to `default`.

```{note}
Cheats must be enabled in order to use this command.
```

```{seealso}
[`savepos`](#savepos)
```

---

## ma, say_admin
Sends a message to [admin chat](../server/admin_system.md/#admin-chat).

`ma <message>`  
`say_admin <message>`

{.option-table}
Option                    | Description
:-------------------------|:------------
**message**               | The message to send.

---

## min, minimize
Minimizes the game. Only works on Windows.

---

## mod_information
Prints the ETJump version the server is running.

---

## moveCustomCommand
Moves a command from the given slot/page to another page/slot.

`moveCustomCommand <from-page (1-5)> <from-slot (1-8)> <to-page (1-5)> [to-slot (1-8)]`

{.option-table}
Option                    | Description
:-------------------------|:------------
**-fp, --from-page**      | The page to move the command from (1-5).
**-fs, --from-slot**      | The slot to move the command from (1-8).
**-tp, --to-page**        | The page to move the command to (1-5).
-ts, --to-slot            | The slot to move the command to (1-8). Defaults to the first free slot on the given page. If the targeted slot already has a command, the commands will be swapped.

```{note}
Swapping commands only happens if `--to-slot` argument is explicitly given. If the targeted page is full, the move fails, unless the target slot is specified (which will swap the commands between from/to pages/slots).
```

---

## nocall
Toggles whether other players are allowed to call you.

---

## nogoto
Toggles whether other players can teleport to you.

---

## ob_list
Lists saved overbounce watcher coordinates.

---

## ob_load
Loads saved overbounce watcher coordinates.

`ob_load [name]`

{.option-table}
Option                    | Description
:-------------------------|:------------
name                      | Name of the coordinates to load. Default is `default`.

---

## ob_reset
Clears the currently loaded overbounce watcher coordinates.

---

## ob_save
Saves currently loaded overbounce watcher coordinates.

`ob_save [name]`

{.option-table}
Option                    | Description
:-------------------------|:------------
name                      | Name for the coordinates to save. Default is `default`.

---

## openCustomCommandMenu
Toggles the custom command menu.

`openCustomCommandMenu [page (1-5)]`

{.option-table}
Option                    | Description
:-------------------------|:------------
page                      | If given, opens directly to the specified page (1-5).

---

## portal
Prints information about the portal gun.

---

## printDemoCompatInfo
Prints currently active compatibility settings during demo playback.

---

## printMapCustomizationInfo
Prints the SHA-1 hashes of custom mapscript and/or custom entity file, currently running on the server.

```{note}
The hashes are calculated with `LF` line endings. If you are comparing the hashes to files you have locally, make sure they are saved with `LF` line endings as well.
```

```{tip}
This can be used during demo playback (starting with demos recorded in ETJump 3.5.0) to display the hashes of the files that were loaded on the server, when the demo was recorded.
```

---

## privateMessage
Opens the private message menu. Messages sent via this menu are quote-printable encoded.

```{seealso}
[Quoted-printable - Wikipedia](https://en.wikipedia.org/wiki/Quoted-printable)
```

---

## rankings
Prints timerun rankings. If no arguments are given, prints top **20** overall rankings.

`rankings [season]`

{.option-table}
Option                    | Description
:-------------------------|:------------
-s, --season              | Season to print rankings for.
-p, --page                | Page of rankings to print.
-ps, --page-size          | Number of rankings per page.

---

## ranks, records, times, top
Prints timerun records with given parameters. If no arguments are given, prints top **3** records for each run in the current map.

`records [run name]`  
`records <map name> <run name>`  
`records <season> <map name> <run name>`

{.option-table}
Option                    | Description
:-------------------------|:------------
-s, --season              | Season to print records for. Default is the overall season.
-m, --map                 | Map to print records for. Default is the current map.
-r, --run                 | Run to print records for.
-p, --page                | Page of records to print.
-ps, --page-size          | Number of records per page. If `run` is provided, defaults to **20**. Max is **100** if provided, **10** otherwise.

```{tip}
`<run name>`, `<map name>` and `<season>` support partial name matching.
```

```{note}
`ranks`, `reconds`, `times` and `top` are all valid aliases for this command.
```

---

## readCustomCommands
Parses custom command menu from the file pointed to by [`etj_ccMenu_filename`](etjump_cvars.md/#etj_ccmenu_filename). You must execute this command to reload changes to the menu when editing the file by hand, outside the game.

---

## readsavepos
Reloads all savepos files in `etjump/savepos` directory.

---

## record-details
Prints detailed information about a timerun record.

`record-details <run name>`  
`record-details <run name> <rank>`  
`record-details <map name> <run name> <rank>`  
`record-details <season name> <map name> <run name> <rank>`

{.option-table}
Option                    | Description
:-------------------------|:------------
**-r, --run**             | Name of the run.
-s, --season              | Name of the season. Default is the overall season.
-m, --map                 | Name of the map. Default is the current map.
-rk, --rank               | Rank to print details for. Defaults to **1**.

---

## record-history
Prints a user's record progression on a timerun.

`record-history <run name>`  
`record-history <map name> <run name>`  
`record-history <season name> <map name> <run name>`  
`record-history <season name> <map name> <run name> <user ID>`

{.option-table}
Option                    | Description
:-------------------------|:------------
**-r, --run**             | Name of the run.
-s, --season              | Name of the season. Default is the overall season.
-m, --map                 | Name of the map.
-u, --user                | User ID of the user whose history to print. Default is your own user.
-p, --page                | Page of record history to print.
-ps, --page-size          | How many records to show on. Defaults to **20**, max is **100**.

```{note}
Historical progression for timerun records is not recorded for any run prior to ETJump 3.7.0.
```

---

## remove-record
Removes a timerun record from the records table.

`remove-record <run name>`  
`remove-record <map name> <run name>`  
`remove-record <season name> <map name> <run name>`

{.option-table}
Option                    | Description
:-------------------------|:------------
**-r, --run**             | Name of the run.
-s, --season              | Name of the season. If not given, defaults to the overall season, cascading to any other season holding a copy of the record.
-m, --map                 | Name of the map.
-u, --user                | User ID of the user whose record to remove.
-re, --reason             | Reason for removing the record. Mandatory when removing other players' records, optional when removing your own.

Any player can remove their own record on a run; administrators with the [`timerun management (T)`](../server/admin_system.md/#permission-system) admin flag can remove records from other players.

```{note}
* All parameters in this command must be an exact match, no partial/fuzzy matching is performed.
* You can view all removed records with the [`list-removed-records`](client_commands.md/#list-removed-records) command.
* Records removed by this command are stored in the removed records archive, and can be restored with the [`restore-record`](client_commands.md/#restore-record) command.
```

---

## remove-segment
Removes a recorded best timerun segment.

`remove-segment <run name> <segment>`  
`remove-segment <map name> <run name> <segment>`  
`remove-segment <season name> <map name> <run name> <segment>`

{.option-table}
Option                    | Description
:-------------------------|:------------
-s, --season              | Season to remove the segment from. Default is the overall season, cascading to any other season holding a copy of the same segment.
-m, --map                 | Map to remove the segment from. Default is the current map.
**-r, --run**             | Run to remove the segment from.
**-sg, --segment**        | The segment to remove.
-u, --user                | User ID of the segment owner. Only administrators (flag `T`) can remove other players' segments. Default is your own user ID.
-re, --reason             | Reason for the removal. Optional when removing your own segments, required when removing another player's segment.

Removed segments are archived in the timerun database, not completely removed.

Map and run names are matched exactly when possible. A partial name is accepted when it resolves to a single map or run.

Administrators with the [`timerun management (T)`](../server/admin_system.md/#permission-system) admin flag can remove another player's segment by adding `--user <user ID> --reason <reason>`.

---

## resetmaxspeed
Resets the maximum speed displayed at speedmeter 1.

---

## resetJumpSpeeds
Queues reset for jump speeds display. This command is automatically executed upon death, team change, [`save`](client_commands.md/#save) and [`load`](client_commands.md/#load). The display will reset on next jump event.

---

## resetStrafeQuality
Queues reset for strafe quality display. This command is automatically executed upon death, team change, [`save`](client_commands.md/#save) and [`load`](client_commands.md/#load). The display will reset the next time you're in air or on slick.

---

## resetUpmoveMeter
Resets the upmove meter display. This command is automatically executed upon death, team change, [`save`](client_commands.md/#save) and [`load`](client_commands.md/#load).

---

## restore-record
Restores a removed timerun record.

`restore-record <ID>`

{.option-table}
Option                    | Description
:-------------------------|:------------
**-i, --id**              | The record ID to restore.
-f, --force               | Forces the restoration in case of a conflict, moving the conflicting record to the removed records database in place of the restored one.

When targeting a record that is present in multiple seasons, the restoration cascades and restores all the copies of the record present in other seasons.

You can only restore records you have removed yourself, unless you have the [`timerun management (T)`](../server/admin_system.md/#permission-system) admin flag.

---

## restore-segment
Restores a removed best timerun segment.

`restore-segment <ID>`

{.option-table}
Option                    | Description
:-------------------------|:------------
**-i, --id**              | The segment ID to restore.
-f, --force               | Forces the restoration in case of a conflict, moving the conflicting segment to the removed segments database in place of the restored one.

Restoring the default season's copy cascades and restores the copies of that same split present in other seasons. Targeting a specific season's copy restores only that season.

You can only restore segments you have removed yourself, unless you have the [`timerun management (T)`](../server/admin_system.md/#permission-system) admin flag.

---

## rtvVote
Casts a vote for the map specified by `<number>` in an ongoing Rock The Vote.

`rtvVote <number>`

{.option-table}
Option                    | Description
:-------------------------|:------------
**number**                | The number of the map to vote for.

---

## save
Saves current position.

`save [slot]`

{.option-table}
Option                    | Description
:-------------------------|:------------
slot                      | The save slot to save to (0-2). Defaults to **0**.

---

## savepos
Saves your current position, angles, velocity, stance and timerun state to a savepos file.

`savepos [name] [flags (0-3)]`

{.option-table}
Option                    | Description
:-------------------------|:------------
name                      | Name of the savepos file. Defaults to `default`.
flags                     | Bitflag value (0-3): **1** resets velocity to 0, **2** resets pitch angle to 0.

If only one argument is given, and the argument is a single number, it is treated as a flag.

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
Offsets your position by the amount of units on each vector. Usage requires access to `noclip`.

`setoffset <x> <y> <z>`

{.option-table}
Option                    | Description
:-------------------------|:------------
**x**                     | Offset on the X axis.
**y**                     | Offset on the Y axis.
**z**                     | Offset on the Z axis.

```{note}
Maximum offset range per vector is **-4096 - 4096**.
```

---

## specinvite, specuninvite
Invites/uninvites specified client to spectate you.

`specinvite <name/clientnum>`  
`specuninvite <name/clientnum>`

{.option-table}
Option                    | Description
:-------------------------|:------------
**<name/clientnum>**      | Name or clientnum of the player to invite/uninvite

---

## speclist
Prints a list of clients who are allowed to spectate you while speclocked.

---

## speclock, specunlock
Locks/unlocks you from spectators. When locked, use `specinvite/specuninvite` to invite/uninvite clients to spectate you.

---

## toggleETJumpSettings
Toggles the ETJump settings menu.

```{hint}
This is simply a shortcut to open `ETJump -> Settings -> General/Gameplay` page. The sole purpose of this command is to be able to bind the settings menu toggle to a key.
```

---

## tracker_print
Prints your current tracker values on given indices. Special case `all` prints tracker values on every index. You may specify multiple indices to print, separated by space.

`tracker_print [index|all] [index2] [index3] ...`

{.option-table}
Option                    | Description
:-------------------------|:------------
index\|all                | The tracker index to print, or `all` to print every index. Defaults to index **1**.

```{note}
Usage of this command requires the server to have [`g_debugTrackers 1`](../server/server_cvars.md/#g_debugtrackers). Timerun records are not saved when tracker debugging is enabled.
```

---

## tracker_set
Sets your tracker on given index to specified value. Special case `all` sets specified value in all indices.

`tracker_set [index|all] <value>`

{.option-table}
Option                    | Description
:-------------------------|:------------
index\|all                | The tracker index to set, or `all` to set every index. Defaults to index **1**.
**value**                 | The value to set the tracker to.

```{note}
Usage of this command requires the server to have [`g_debugTrackers 1`](../server/server_cvars.md/#g_debugtrackers). Timerun records are not saved when tracker debugging is enabled.
```

---

## unload
Undo your last [`load`](client_commands.md/#load) command and teleport back to the position you last executed a load from. The position must be a valid position for using [`save`](client_commands.md/#save) (e.g. cannot use `unload` to teleport to an area where you cannot `save`).

```{note}
`unload` cannot be used during timeruns. There is only a single slot available, which is overwritten on every successful `load` command.
```
