# List of ETJump admin commands
Below is a list of all ETJump related admin commands.

## 8ball
`!8ball [question]`  
8ball answers all your questions with three possible answers: yes, no and maybe.

---

## addlevel
`!addlevel [level] -cmds [commands] -greeting [greeting] -title [title]`  
Adds a new level. Optionally you can use -cmds, -greeting and -title switches to set commands, greeting and title.

---

## admintest
`!admintest`  
Prints your admin level to everyone in the chat.

---

## ban
`!ban [player] [time] [reason]`  
Bans a player. Optionally you can set a time for ban duration in seconds. No time means a permanent ban. Optionally you can also give a reason for the ban that will be printed to the banned user. Setting a reason requires and time as well.

---

## cancelvote
`!cancelvote`  
Cancels the current vote.

---

## deletelevel
`!deletelevel [level]`  
Deletes a level. Finds every user with that level and sets them to level 0.

---

## editcommands
`!editcommands [level] +[command] -[command]`  
Edits a single level's commands. Adding a + before the command will add that command to the level, adding a - before the command will remove that command from the level. The following example adds kick and ban to level 5 and removes 8ball from the level 5. `!editcommands 5 +kick +ban -8ball`

---

## editlevel
`!editlevel [level] -cmds [commands] -greeting [greeting] -title [title] -clear cmds,greeting,title`  
Edits a level. `-cmds [command flags]` to edit commands, `-greeting [greeting]`o edit greeting, `-title [title]` to edit title. To empty commands, greeting or title do for example `-clear cmds`.

---

## edituser
`!edituser [id] -cmds [commands] -greeting [greeting] -title [title] -clear cmds, greeting, title`  
Edits user's private commands, greeting or title. `-cmds [command flags]` to edit commands, `-greeting [greeting]` to edit greeting, `-title [title]` to edit title. `-clear cmds` to empty commands.

---

## findmap
`!findmap [partial name] [maps per row]`  
Lists all maps on server matching __[partial name]__. Use __[maps per row]__ to define how many maps are listed per row.

---

## finduser
`!finduser [name]`  
Lists users that match the name.

---

## finger
`!finger [name]`  
Prints information about target player.

---

## help
`!help [command]`  
Prints a list of commands if no parameter is given. If a parameter is given, prints the manual of given command.

---

## kick
`!kick [player]`  
Kicks target player.

---

## leastplayed
`!leastplayed`  
Lists __5__ of the least played maps.

---

## levelinfo
`!levelinfo [level]`  
Lists all levels if no level is given. If a level is given, prints information of that level.

---

## listbans
`!listbans [page]`  
Lists bans. If no page is given, lists latest bans.

---

## listflags
`!listflags`  
Lists command flags for each admin command.

---

## listmaps
`!listmaps`  
Lists all maps on the server.

---

## listusernames
`!listusernames [id]`  
Lists all names player with id has used on the server.

---

## listusers
`!listusers [page]`  
Lists users that have visited the server. If a page is given, lists users on that page. Max __20__ users per page.

---

## map
`!map [map]`  
Changes map to target map.

---

## mapinfo
`!mapinfo [map]`  
Lists information about target map.

---

## mostplayed
`!mostplayed`  
Lists __5__ most played maps.

---

## mute
`!mute [player]`  
Mutes target player.

---

## noclip
`!noclip [player] [count]`  
Gives noclip to player. If count is specified, allows player to use noclip `[count]` times.

---

## nogoto
`!nogoto [player]`  
Enable and disable goto for target player.

---

## nosave
`!nosave [player]`  
Enable and disable save for target player.

---

## passvote
`!passvote`  
Passes current vote.

---

## putteam
`!putteam [player] [team]`  
Puts target player to team.

---

## rename
`!rename [player] [new name]`  
Renames target player.

---

## restart
`!restart`  
Restarts current map.

---

## rmsaves
`!rmsaves [player]`  
Resets saved position for target player.

---

## setlevel
`!setlevel [player] [level] or -id [id] [level]`  
Sets target player or player with id to level.

---

## spectate
`!spectate [player]`  
Spectates target player.

---

## unban
`!unban [ban id]`  
Removes ban with __ID__. __ID__ can be checked with the `!listbans` command.

---

## unmute
`!unmute [player]`  
Unmutes target player.

---

## userinfo
`!userinfo [id]`  
Prints information about user.