# List of ETJump admin commands
Below is a list of all ETJump related admin commands.

---

## 8ball
`!8ball [question]`  
8ball answers all your questions with three possible answers: yes, no and maybe.

**Flag:** a

---

## add-customvote
`!add-customvote --name [name] [required] --full-name [callvote_text] [required] --maps [maps] [required]`  
Adds a new custom map vote list. `[maps]` is a space separated list of maps to include in the list.

**Flag:** c

---

## add-season
`!add-season --name [name] [required] --start-date [YYYY-MM-DD] [required] --end-date-exclusive [YYYY-MM-DD]`  
Adds a new timerun season. If `--end-date-exclusive` isn't set, the season will be active until end date is added with [`!edit-season`](admin_system.md/#edit-season).

_Note: season names are case insensitive._

**Flag:** T

---

## addlevel
`!addlevel [level] -cmds [commands] -greeting [greeting] -title [title]`  
Adds a new level. Optionally you can use `-cmds`, `-greeting` and `-title` switches to set commands, greeting and title.

**Flag:** A

---

## admintest
`!admintest`  
Prints your admin level to everyone in the chat.

**Flag:** a

---

## ban
`!ban [player] [time] [reason]`  
Bans a player. Optionally you can set a time for ban duration in seconds. No time means a permanent ban. Optionally you can also give a reason for the ban that will be printed to the banned user. Setting a reason requires and time as well.

**Flag:** b

---

## cancelvote
`!cancelvote`  
Cancels the current vote.

**Flag:** C

---

## delete-customvote
`!delete-customvote --name [name]`  
Deletes a custom map vote list. Name must be an exact match.

**Flag:** c

---

## delete-season
`!delete-season --name [exact name]`  
Deletes a timerun season. Name must be an exact match.

_Note: this will delete all timerun records associated with the season. Season names are case insensitive._

**Flag:** T

---

## deletelevel
`!deletelevel [level]`  
Deletes a level. Users who are currently set to deleted level will be set to level 0.

**Flag:** A

---

## edit-customvote
`!edit-customvote --list [name] [required] --name [name] --full-name [callvote_text] --add-maps [maps] --remove-maps [maps]`  
Edits an existing custom map vote list.

**Flag:** c

---

## edit-season
`!edit-season --name [name] [required] --start-date [YYYY-MM-DD] --end-date [YYYY-MM-DD]`  
Edits an existing timerun season.

_Note: season names are case insensitive._

**Flag:** T

---

## editcommands
`!editcommands [level] +[command] -[command]`  
Edits a single level's commands. Adding a + before the command will add that command to the level, adding a - before the command will remove that command from the level. The following example adds kick and ban to level 5 and removes 8ball from the level 5. `!editcommands 5 +kick +ban -8ball`

**Flag:** A

---

## editlevel
`!editlevel [level] -cmds [commands] -greeting [greeting] -title [title] -clear cmds,greeting,title`  
Edits a level. `-cmds [command flags]` to edit commands, `-greeting [greeting]`o edit greeting, `-title [title]` to edit title. To empty commands, greeting or title do for example `-clear cmds`.

**Flag:** A

---

## edituser
`!edituser [id] -cmds [commands] -greeting [greeting] -title [title] -clear cmds, greeting, title`  
Edits user's private commands, greeting or title. `-cmds [command flags]` to edit commands, `-greeting [greeting]` to edit greeting, `-title [title]` to edit title. `-clear cmds` to empty commands.

**Flag:** A

---

## findmap
`!findmap [partial name] [maps per row]`  
Lists all maps on server matching **[partial name]**. Use **[maps per row]** to define how many maps are listed per row.

**Flag:** a

---

## finduser
`!finduser [name]`  
Lists users that match the name.

**Flag:** A

---

## finger
`!finger [name]`  
Prints information about target player.

**Flag:** f

---

## help
`!help [command]`  
Prints a list of commands if no parameter is given. If a parameter is given, prints the manual of given command.

**Flag:** a

---

## kick
`!kick [player]`  
Kicks target player.

**Flag:** k

---

## leastplayed
`!leastplayed [count]`  
Lists the least played maps on the server. If no `[count]` is given, defaults to **5** maps. Maximum number of maps to list is **100**.

**Flag:** a

---

## levelinfo
`!levelinfo [level]`  
Lists all levels if no level is given. If a level is given, prints information of that level.

**Flag:** A

---

## listbans
`!listbans [page]`  
Lists bans. If no page is given, lists latest bans.

**Flag:** L

---

## listflags
`!listflags`  
Lists command flags for each admin command.

**Flag:** A

---

## listmaps
`!listmaps`  
Lists all maps on the server.

**Flag:** a

---

## listplayers
`!listplayers`  
Lists all players on server.

**Flag:** l

---

## listusernames
`!listusernames [id]`  
Lists all names player with id has used on the server.

**Flag:** A

---

## listusers
`!listusers [page]`  
Lists users that have visited the server. If a page is given, lists users on that page. Max **20** users per page.

**Flag:** A

---

## loadcheckpoints, load-checkpoints
`!loadcheckpoints [run name]`  
`!loadcheckpoints [run name] [rank]`  
Loads timerun checkpoints for comparison for given timerun. If `[rank]` isn't specified, defaults to rank 1 time. Loaded checkpoints can be cleared by specifying `-1` as rank. `[run name]` supports partial matching.

**Flag:** a

---

## map
`!map [map]`  
Changes map to target map.

**Flag:** M

---

## mapinfo
`!mapinfo [map]`  
Lists information about target map.

**Flag:** a

---

## mostplayed
`!mostplayed [count]`
Lists the most played maps on the server. If no `[count]` is given, defaults to **5** maps. Maximum number of maps to list is **100**.

**Flag:** a

---

## moverscale
`!moverscale [value]`  
Scales vehicle movement speed by given value. Valid range is **0.1-5.0**.

**Flag:** v

---

## mute
`!mute [player]`  
Mutes target player.

**Flag:** m

---

## newmaps
`!newmaps [count]`  
Displays the latest `[count]` maps added to the server, sorted from oldest to newest.  Maximum number of maps to list is **50**.

**Flag:** a

---

## noclip
`!noclip [player] [count]`  
Gives noclip to player. If count is specified, allows player to use noclip `[count]` times.

**Flag:** N

---

## passvote
`!passvote`  
Passes current vote.

**Flag:** P

---

## rankings
`!rankings [season]`  
`!rankings --season [season] --page [page] --page-size [page size]`  
Prints timerun rankings. If no parameters are given, prints top **20** overall rankings.

**Flag:** a

---

## ranks, records, times and top
`!records [run name]`  
`!records [map name] [run name]`  
`!records [season] [map name] [run name]`  
`!records --season [season] --map [map name] --run [run name] --page [page] --page-size [page size]`  
Prints timerun records with given parameters. If `[run name]` isn't specified, prints top **3** records of all timeruns in the map. If specified, will print top **20** records for given run. If `[season]` isn't specifed, prints overall records. `[run name]`, `[map name]` and `[season]` support partial name matching.

_Note: `!ranks`, `!reconds`, `!times` and `!top` are all valid aliases for this command._

**Flag:** a

---

## rename
`!rename [player] [new name]`  
Renames target player.

**Flag:** R

---

## restart
`!restart`  
Restarts current map.

**Flag:** r

---

## rtv
`!rtv`  
Calls Rock The Vote.

**Flag:** a

---

## seasons
`!seasons`  
Lists all timerun seasons on the server.

**Flag:** a

---

## setlevel
`!setlevel [player] [level] or -id [id] [level]`  
Sets target player or player with id to level.

**Flag:** s

---

## spectate
`!spectate [player]`  
Spectates target player.

**Flag:** a

---

## tokens
`!tokens create [easy (e)|medium (m)|hard (h)]` 

`!tokens move` 

`!tokens delete`

`!tokens delete [easy (e)|medium (m)|hard (h)] [1-6]` 

Creates/deletes a collectible token with given parameters. You can create maximum of **6** tokens per difficulty. `!tokens move` moves nearest token to your location. `!tokens delete` deletes a token nearest to your location.

**Flag:** V

---

## unban
`!unban [ban id]`  
Removes ban with **ID**. **ID** can be checked with the `!listbans` command.

**Flag:** b

---

## unmute
`!unmute [player]`  
Unmutes target player.

**Flag:** m

---

## userinfo
`!userinfo [id]`  
Prints information about user.

**Flag:** A

---

## Silent command execution
`/!command`  
Allows clients to execute any admin commands available to them silently, without having the typed command appear in chat.

*Note: Must be typed in console. Any output that the given command produces might still be visible to other clients.*

**Flag:** /

---
