# List of ETJump server cvars
Below is a list of all ETJump related cvars (console variables) for server configuration.

---

## g_adminLog
Name                    | values        | default
------------------------|:-------------:|-------------
g_adminLog              | filename      | adminsystem.log

Logs admin commands in a separate log if `g_log` is set.

---

## g_banDatabase
Name                    | values        | default
------------------------|:-------------:|-------------
g_banDatabase           | filename      | bans.dat

File where bans are stored. Filename is currently hardcoded into mod and cannot be changed.

---

## g_bannerN
Name                    | values        | default
------------------------|:-------------:|-------------
g_bannerN               | any text      |

Where N is a number from 1 to 5. Text to print out in a banner.

---

## g_bannerLocation
Name                    | values        | default
------------------------|:-------------:|-------------
g_bannerLocation        | 0 - 3         | 1

Sets the location where banners are printed.

* __0__ for center print, 
* __1__ for top print, 
* __2__ for chat print, 
* __3__ for left print.

---

## g_bannerTime
Name                    | values        | default
------------------------|:-------------:|-------------
g_bannerTime            | any integer   | 60000

How often in milliseconds to print banners.

---

## g_banners
Name                    | values        | default
------------------------|:-------------:|-------------
g_banners               | 0 or 1        | 0

Toggles banners.

---

## g_blockCheatCvars
Name                    | values        | default
------------------------|:-------------:|-------------
g_blockCheatCvars       | 0 or 1        | 0

Toggles whether to block cvars that could be considered cheating such:

* __m_pitch__ (-0.01 <= x <= 0.01)
* __cl_yawspeed__ (not 0)
* __cl_freelook__ (0)
* __pmove_Fixed__ (0) while having
* __com_maxFPS__ (25 < x or x > 125)

---

## g_blockedMaps
Name                    | values        | default
------------------------|:-------------:|-------------
g_blockedMaps           | map names     | 

A list of maps that cannot be voted for. Names are separated by space. Use .bsp names.

---

## g_chatOptions
Name                    | values        | default
------------------------|:-------------:|-------------
g_chatOptions           | 0 or 1        | 1

Allow players to highlight other players in chat using @name@.

---

## g_customMapVotesFile
Name                    | values        | default
------------------------|:-------------:|-------------
g_customMapVotesFile    | filename      | customvotes.json

Filename for the custom map votes file.

---

## g_customVoiceChat
Name                    | values        | default
------------------------|:-------------:|-------------
g_customVoiceChat       | 0 or 1        | 1

Enables custom text for voice chats.

---

## g_dailyLogs
Name                    | values        | default
------------------------|:-------------:|-------------
g_dailyLogs             | 0 or 1        | 1

Whether to log everything in a single file or change the file daily.

---

## g_debugTimeruns
Name                    | values        | default
------------------------|:-------------:|-------------
g_debugTimeruns         | 0 or 1        | 0

Toggles timerun debugging. When enabled, allows players to use cheats during timeruns, but records are not saved.

---

## g_debugTrackers
Name                    | values        | default
------------------------|:-------------:|-------------
g_debugTrackers         | 0 or 1        | 0

Toggles tracker debugging. When enabled, all tracker changes are printed to players. Additionally, players gain access to following commands:

* `tracker_print [index1|all] [index2] [index3]...` prints tracker values on specified or all indices. If index isn't specified, defaults to index __1__.
* `tracker_set [index|all] [value]` sets tracker on specified index to specified value. If index is not specified, defaults to index __1__.

Timerun records are not saved when tracker debugging is enabled.

---

## g_disableVoteAfterMapChange
Name                    | values        | default
------------------------|:-------------:|-------------
g_disableVoteAfterMapChange | any integer | 30000

How long players must wait to vote again in milliseconds after map changes.

---

## g_enableVote
Name                    | values        | default
------------------------|:-------------:|-------------
g_enableVote            | 0 or 1        | 1

Toggles voting.

---

## g_floodlimit
Name                    | values        | default
------------------------|:-------------:|-------------
g_floodlimit            | any integer   | 5

How many times can player send a message fast before flood protection kicks in.

---

## g_floodprotection
Name                    | values        | default
------------------------|:-------------:|-------------
g_floodprotection       | 0 or 1        | 1

Toggles flood protection.

---

## g_floodwait
Name                    | values        | default
------------------------|:-------------:|-------------
g_floodwait             | any integer   | 768

Time in milliseconds to allow player to send messages again.

---

## g_ghostPlayers
Name                    | values        | default
------------------------|:-------------:|-------------
g_ghostPlayers          | 0 or 1        | 1

Toggles whether players can go through each other.

---

## g_goto
Name                    | values        | default
------------------------|:-------------:|-------------
g_goto                  | 0 or 1        | 1

Toggles goto.

---

## g_lastVisitedMessage
Name                    | values        | default
------------------------|:-------------:|-------------
g_lastVisitedMessage    | any text      | ^2Welcome back! Your last visit was on [t].

Message that prints to returning players.

---

## g_levelConfig
Name                    | values        | default
------------------------|:-------------:|-------------
g_levelConfig           | filename      | levels.cfg

File to store levels in.

---

## g_mapDatabase
Name                    | values        | default
------------------------|:-------------:|-------------
g_mapDatabase           | filename      | maps.dat

File where information about maps is stored (eg. playtime).

---

## g_mapScriptDir
Name                    | values        | default
------------------------|:-------------:|-------------
g_mapScriptDir          | directory name | mapscripts

Directory to load custom map scripts from.

---

## g_maxConnsPerIP
Name                    | values        | default
------------------------|:-------------:|-------------
g_maxConnsPerIP         | any integer   | 2

How many clients can connect from a single IP address.

---

## g_motdFile
Name                    | values        | default
------------------------|:-------------:|-------------
g_motdFile              | filename     | motd.json

File that has the message of the day.

---

## g_moverScale
Name                    | values        | default
------------------------|:-------------:|-------------
g_moverScale            | 0.1 - 5.0     | 1.0

Scales movement speed of vehicles. Can be also accessed with `!moverscale` admin command.

---

## g_mute
Name                    | values        | default
------------------------|:-------------:|-------------
g_mute                  | 0 - 3         | 0

Mute behaviour. 

* __0__ default behaviour. 
* __1__ disable private messages. 
* __2__ disable callvote. 
* __3__ disable both.

---

## g_nameChangeInterval
Name                    | values        | default
------------------------|:-------------:|-------------
g_nameChangeInterval    | any integer   | 60

How often in seconds is the name change limit reseted.

---

## g_nameChangeLimit
Name                    | values        | default
------------------------|:-------------:|-------------
g_nameChangeLimit       | any integer   | 5

How many times user can change name.

---

## g_noclip
Name                    | values        | default
------------------------|:-------------:|-------------
g_noclip                | 0 or 1        | 0

Toggles noclip for players.

---

## g_nofatigue
Name                    | values        | default
------------------------|:-------------:|-------------
g_nofatigue             | 0 or 1        | 1

Toggles nofatigue for players.

---

## g_oss
Name                    | values        | default
------------------------|:-------------:|-------------
g_oss                   | bitflag       | 15

Indicates operating systems and architectures supported by the mod. This is intended for ET: Legacy server browser to filter out mods that are incompatible with clients OS/architecture, and should be left unchanged.

* __0__ vanilla/unknown/ET: Legacy auto setup
* __1__ Windows 32-bit
* __2__ Linux 32-bit
* __4__ Linux 64-bit
* __8__ Mac OS X (Intel, 64-bit)
* __16__ Android
* __32__ Raspberry Pi

---

## g_portalDebug
Name                    | values        | default
------------------------|:-------------:|-------------
g_portalDebug           | 0 or 1        | 0

Toggles drawing of portal activation box.

---

## g_portalMode
Name                    | values        | default
------------------------|:-------------:|-------------
g_portalMode            | 0 or 1        | 1

Toggles restricted portal gun mode. 

* __0__ to give portal gun to players on spawn. 
* __1__ to disable.

---

## g_raceDatabase
Name                    | values        | default
------------------------|:-------------:|-------------
g_raceDatabase          | filename      | races.db

File where information about races is stored in. Filename is currently hardcoded into mod and cannot be changed.

---

## g_save
Name                    | values        | default
------------------------|:-------------:|-------------
g_save                  | 0 or 1        | 1

Toggles save and load.

---

## g_spectatorVote
Name                    | values        | default
------------------------|:-------------:|-------------
g_spectatorVote         | 0 - 2         | 0

Toggles spectator voting.

* __1__ spectators can cast votes.
* __2__ spectators can also call votes.

_Note: Only spectators who participate in voting are taken into account by `vote_percent` cvar, to prevent votes never passing on servers with multiple idle spectators._

---

## g_timerunsDatabase
Name                    | values        | default
------------------------|:-------------:|-------------
g_timerunsDatabase      | filename     | timeruns.db

File to store timeruns data in.

---

## g_tokensMode
Name                    | values        | default
------------------------|:-------------:|-------------
g_tokensMode            | 0 or 1        | 1

Enables players to use `!tokens` command to add collectible tokens into a map. 

---

## g_tokensPath
Name                    | values        | default
------------------------|:-------------:|-------------
g_tokensPath            | directory name| tokens

Directory where tokens information is stored.

---

## g_userConfig
Name                    | values        | default
------------------------|:-------------:|-------------
g_userConfig            | filename     | users.db

File to store user data in.

---

## g_voteCooldown
Name                    | values        | default
------------------------|:-------------:|-------------
g_voteCooldown          | any integer   | 15

How long must a player wait to call another vote.

---

## g_weapons
Name                    | values        | default
------------------------|:-------------:|-------------
g_weapons               | 0 or 1        | 1

Toggles whether players spawn with weapons or just knife.

---

## vote_allow_randommap
Name                    | values        | default
------------------------|:-------------:|-------------
vote_allow_randommap    | 0 or 1        | 1

Toggles whether players can vote for a random map.

---

## vote_minVoteDuration
Name                    | values        | default
------------------------|:-------------:|-------------
vote_minVoteDuration    | any integer   | 5000

Minimum time in milliseconds a vote must active before passing.

---
