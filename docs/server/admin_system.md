# List of ETJump admin commands
Below is a list of all ETJump related admin commands.

---

## 8ball
`!8ball [question]`  
8ball answers all your questions with three possible answers: yes, no and maybe.

__Flag:__ a

---

## addlevel
`!addlevel [level] -cmds [commands] -greeting [greeting] -title [title]`  
Adds a new level. Optionally you can use -cmds, -greeting and -title switches to set commands, greeting and title.

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

## deletelevel
`!deletelevel [level]`  
Deletes a level. Finds every user with that level and sets them to level 0.

__Flag:__ A

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
`!leastplayed`  
Lists __5__ of the least played maps.

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
`!mostplayed`  
Lists __5__ most played maps.

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

## noclip
`!noclip [player] [count]`  
Gives noclip to player. If count is specified, allows player to use noclip `[count]` times.

__Flag:__ N

---

## nogoto
`!nogoto [player]`  
Enable and disable goto for target player.

__Flag:__ K

---

## nosave
`!nosave [player]`  
Enable and disable save for target player.

__Flag:__ T

---

## passvote
`!passvote`  
Passes current vote.

__Flag:__ P

---

## putteam
`!putteam [player] [team]`  
Puts target player to team.

__Flag:__ p

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

## rmsaves
`!rmsaves [player]`  
Resets saved position for target player.

__Flag:__ T

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
