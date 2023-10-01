# List of ETJump admin commands
Below is a list of all ETJump related admin commands.

---

## 8ball
`!8ball [question]`  
8ball answers all your questions with three possible answers: yes, no and maybe.

__Flag:__ a

---

## add-season
`!add-season --name [name] [required] --start-date [YYYY-MM-DD] [required] --end-date-exclusive [YYYY-MM-DD]`  
Adds a new timerun season. If `--end-date-exclusive` isn't set, the season will be active until end date is added with [`!edit-season`](admin_system.md/#edit-season).

_Note: season names are case insensitive._

__Flag:__ T

---

## addlevel
`!addlevel [level] -cmds [commands] -greeting [greeting] -title [title]`  
Adds a new level. Optionally you can use `-cmds`, `-greeting` and `-title` switches to set commands, greeting and title.

__Flag:__ A

---

## admintest
`!admintest`  
Prints your admin level to everyone in the chat.

__Flag:__ a

---

## ban
`!ban [player] [time] [reason]`  
Bans a player. Optionally you can set a time for ban duration in seconds. No time means a permanent ban. Optionally you can also give a reason for the ban that will be printed to the banned user. Setting a reason requires and time as well.

__Flag:__ b

---

## cancelvote
`!cancelvote`  
Cancels the current vote.

__Flag:__ C

---

## delete-season
`!delete-season --name [exact name]`  
Deletes a timerun season. Name must be an exact match.

_Note: this will delete all timerun records associated with the season. Season names are case insensitive._

__Flag:__ T

---

## deletelevel
`!deletelevel [level]`  
Deletes a level. Users who are currently set to deleted level will be set to level 0.

__Flag:__ A

---

## edit-season
`!edit-season --name [name] [required] --start-date [YYYY-MM-DD] --end-date [YYYY-MM-DD]`  
Edits an existing timerun season.

_Note: season names are case insensitive._

__Flag:__ T

---

## editcommands
`!editcommands [level] +[command] -[command]`  
Edits a single level's commands. Adding a + before the command will add that command to the level, adding a - before the command will remove that command from the level. The following example adds kick and ban to level 5 and removes 8ball from the level 5. `!editcommands 5 +kick +ban -8ball`

__Flag:__ A

---

## editlevel
`!editlevel [level] -cmds [commands] -greeting [greeting] -title [title] -clear cmds,greeting,title`  
Edits a level. `-cmds [command flags]` to edit commands, `-greeting [greeting]`o edit greeting, `-title [title]` to edit title. To empty commands, greeting or title do for example `-clear cmds`.

__Flag:__ A

---

## edituser
`!edituser [id] -cmds [commands] -greeting [greeting] -title [title] -clear cmds, greeting, title`  
Edits user's private commands, greeting or title. `-cmds [command flags]` to edit commands, `-greeting [greeting]` to edit greeting, `-title [title]` to edit title. `-clear cmds` to empty commands.

__Flag:__ A

---

## findmap
`!findmap [partial name] [maps per row]`  
Lists all maps on server matching __[partial name]__. Use __[maps per row]__ to define how many maps are listed per row.

__Flag:__ a

---

## finduser
`!finduser [name]`  
Lists users that match the name.

__Flag:__ A

---

## finger
`!finger [name]`  
Prints information about target player.

__Flag:__ f

---

## help
`!help [command]`  
Prints a list of commands if no parameter is given. If a parameter is given, prints the manual of given command.

__Flag:__ a

---

## kick
`!kick [player]`  
Kicks target player.

__Flag:__ k

---

## leastplayed
`!leastplayed [count]`  
Lists the least played maps on the server. If no `[count]` is given, defaults to __5__ maps. Maximum number of maps to list is __100__.

__Flag:__ a

---

## levelinfo
`!levelinfo [level]`  
Lists all levels if no level is given. If a level is given, prints information of that level.

__Flag:__ A

---

## listbans
`!listbans [page]`  
Lists bans. If no page is given, lists latest bans.

__Flag:__ L

---

## listflags
`!listflags`  
Lists command flags for each admin command.

__Flag:__ A

---

## listmaps
`!listmaps`  
Lists all maps on the server.

__Flag:__ a

---

## listplayers
`!listplayers`  
Lists all players on server.

__Flag:__ l

---

## listusernames
`!listusernames [id]`  
Lists all names player with id has used on the server.

__Flag:__ A

---

## listusers
`!listusers [page]`  
Lists users that have visited the server. If a page is given, lists users on that page. Max __20__ users per page.

__Flag:__ A

---

## loadcheckpoints, load-checkpoints
`!loadcheckpoints [run name]`  
`!loadcheckpoints [run name] [rank]`  
Loads timerun checkpoints for comparison for given timerun. If `[rank]` isn't specified, defaults to rank 1 time. Loaded checkpoints can be cleared by specifying `-1` as rank. `[run name]` supports partial matching.

__Flag:__ a

---

## map
`!map [map]`  
Changes map to target map.

__Flag:__ M

---

## mapinfo
`!mapinfo [map]`  
Lists information about target map.

__Flag:__ a

---

## mostplayed
`!mostplayed [count]`
Lists the most played maps on the server. If no `[count]` is given, defaults to __5__ maps. Maximum number of maps to list is __100__.

__Flag:__ a

---

## moverscale
`!moverscale [value]`  
Scales vehicle movement speed by given value. Valid range is __0.1-5.0__.

__Flag:__ v

---

## mute
`!mute [player]`  
Mutes target player.

__Flag:__ m

---

## newmaps
`!newmaps [count]`  
Displays the latest `[count]` maps added to the server, sorted from oldest to newest.  Maximum number of maps to list is __50__.

__Flag:__ a

---

## noclip
`!noclip [player] [count]`  
Gives noclip to player. If count is specified, allows player to use noclip `[count]` times.

__Flag:__ N

---

## passvote
`!passvote`  
Passes current vote.

__Flag:__ P

---

## rankings
`!rankings [season]`  
`!rankings --season [season] --page [page] --page-size [page size]`  
Prints timerun rankings. If no parameters are given, prints top **20** overall rankings.

__Flag:__ a

---

## ranks, records, times and top
`!records [run name]`  
`!records [map name] [run name]`  
`!records [season] [map name] [run name]`  
`!records --season [season] --map [map name] --run [run name] --page [page] --page-size [page size]`  
Prints timerun records with given parameters. If `[run name]` isn't specified, prints top **3** records of all timeruns in the map. If specified, will print top **20** records for given run. If `[season]` isn't specifed, prints overall records. `[run name]`, `[map name]` and `[season]` support partial name matching.

_Note: `!ranks`, `!reconds`, `!times` and `!top` are all valid aliases for this command._

__Flag:__ a

---

## rename
`!rename [player] [new name]`  
Renames target player.

__Flag:__ R

---

## restart
`!restart`  
Restarts current map.

__Flag:__ r

---

## seasons
`!seasons`  
Lists all timerun seasons on the server.

__Flag:__ a

---

## setlevel
`!setlevel [player] [level] or -id [id] [level]`  
Sets target player or player with id to level.

__Flag:__ s

---

## spectate
`!spectate [player]`  
Spectates target player.

__Flag:__ a

---

## tokens
`!tokens create [easy (e)|medium (m)|hard (h)]` 

`!tokens move` 

`!tokens delete`

`!tokens delete [easy (e)|medium (m)|hard (h)] [1-6]` 

Creates/deletes a collectible token with given parameters. You can create maximum of __6__ tokens per difficulty. `!tokens move` moves nearest token to your location. `!tokens delete` deletes a token nearest to your location.

__Flag:__ V

---

## unban
`!unban [ban id]`  
Removes ban with __ID__. __ID__ can be checked with the `!listbans` command.

__Flag:__ b

---

## unmute
`!unmute [player]`  
Unmutes target player.

__Flag:__ m

---

## userinfo
`!userinfo [id]`  
Prints information about user.

__Flag:__ A

---

## Silent command execution
`/!command`  
Allows clients to execute any admin commands available to them silently, without having the typed command appear in chat.

*Note: Must be typed in console. Any output that the given command produces might still be visible to other clients.*

__Flag:__ /

---
