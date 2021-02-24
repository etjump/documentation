# List of ETJump client cvars
Below is a list of all ETJump related cvars (console variables) available for players.

---

## b_demo_lookat
Name                    | values        | default
------------------------|:-------------:|-------------
b_demo_lookat           | any integer   | -1

Specifies a client to focus freecam at on demo playback. __-1__ disables focus.

_Note: this cvar shares it's name with the ETPro variant for Camtrace 3D compatibility._

---

## etj_altScoreboard
Name                    | values        | default
------------------------|:-------------:|-------------
etj_altScoreboard       | 0 - 3         | 0

Changes the scoreboard to an alternative one.  

* __0__ default ETMain styled scoreboard.
* __1__ and __2__ draw alternatively styled scoreboard.
* __3__ draws a compact scoreboard with dynamic size and position adjustments.

---

## etj_ad_savePBOnly
Name                    | values        | default
------------------------|:-------------:|-------------
etj_ad_savePBOnly       | 0 or 1        | 0

Whether or not autodemo should save a demo when finishing a timerun.

* __0__ save all demos.
* __1__ save only personal bests.

---

## etj_ad_stopDelay
Name                    | values        | default
------------------------|:-------------:|-------------
etj_ad_stopDelay        | 0 - 10000     | 2000

Time in milliseconds to delay the stopping and saving of autodemo when a timerun ends.

---

## etj_ad_targetPath
Name                    | values        | default
------------------------|:-------------:|-------------
etj_ad_targetPath       | any string    | autodemo

Folder inside `demos` folder to store saved autodemo recordings in.

---

## etj_autoDemo
Name                    | values        | default
------------------------|:-------------:|-------------
etj_autoDemo            | 0 - 2         | 0

Automatically start recording a demo whenever player loads (unless a timerun is active) or spawns.

* __1__ enabled only for maps with a timerun.
* __2__ enabled for all maps.

_Note: Autodemo will keep a maximum of 20 temp demos, located in `demos/temp` before it starts overwriting them._

---

## etj_autoLoad
Name                    | values        | default
------------------------|:-------------:|-------------
etj_autoLoad            | 0 or 1        | 1

Automatically load into last saved position when joining a team.

---

## etj_CGaz5Color1
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGaz5Color1         | [any color](/index.md#color-system) | 0.75 0.75 0.75 1.0

Sets the no accel zone color of CGaz HUD __5__.

---

## etj_CGaz5Color2
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGaz5Color2         | [any color](/index.md#color-system) | 0.0 1.0 0.0 1.0

Sets the minimum angle color of CGaz HUD __5__.

---

## etj_CGaz5Color3
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGaz5Color3         | [any color](/index.md#color-system) | 0.0 0.2 0.0 1.0

Sets the accel zone color of CGaz HUD __5__.

---

## etj_CGaz5Color4
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGaz5Color4         | [any color](/index.md#color-system) | 1.0 1.0 0.0 1.0

Sets the max angle color of CGaz HUD __5__.

---

## etj_CGaz5Fov
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGaz5Fov            | 0 - 180       | 0

Sets the FOV of CGaz HUD __5__. __0__ means use your current in-game FOV.

---

## etj_CGazAlpha
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGazAlpha           | 0.0 - 1.0     | 0.15

Controls CGaz meter transparency.

_Note: This also affects SnapHUD alpha._

---

## etj_CGazColor1
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGazColor1          | [any color](/index.md#color-system) | 1.0 0.0 0.0 1.0

Set the primary color of CGaz HUD __2__.

_Note: value includes alpha._

---

## etj_CGazColor2
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGazColor2          | [any color](/index.md#color-system) | 0.0 1.0 1.0 1.0

Set the secondary color of CGaz HUD __2__.

_Note: value includes alpha._

---

## etj_CGazHeight
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGazHeight          | any integer   | 20

Height of the CGaz meter.

---

## etj_CGazWidth
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGazWidth           | any integer   | 300

Width of the CGaz meter.

---

## etj_CGazY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGazY               | any integer   | 260

Vertical position of CGaz meter.

---

## etj_chatAlpha
Name                    | values        | default
------------------------|:-------------:|-------------
etj_chatAlpha           | 0.0 - 1.0     | 1.0

Set chat transparency.

---

## etj_chatBackgroundAlpha
Name                    | values        | default
------------------------|:-------------:|-------------
etj_chatBackgroundAlpha | 0.0 - 1.0     | 0.33

Controls chat box background transparency.

---

## etj_chatFlags
Name                    | values        | default
------------------------|:-------------:|-------------
etj_chatFlags           | 0 or 1        | 1

Toggles chat flags.

---

## etj_chatLineWidth
Name                    | values        | default
------------------------|:-------------:|-------------
etj_chatLineWidth       | 1 - 200       | 62

Set number of characters on one line of chat before linebreak happens.

---

## etj_chatPosX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_chatPosX            | any integer   | 0

Chat box horizontal offset.

---

## etj_chatPosY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_chatPosY            | any integer   | 0

Chat box vertical offset.

---

## etj_chatScale
Name                    | values        | default
------------------------|:-------------:|-------------
etj_chatScale           | any value     | 1.0

Scales the chat size.

---

## etj_chatShadow
Name                    | values        | default
------------------------|:-------------:|-------------
etj_chatShadow          | 0 or 1        | 0

Draw shadow on chat.

---

## etj_CHS1Info__X__
Where __X__ stands for integer of __1__ to __8__ specifing text position on the circle.
See full list of parameters [here](/index.md#chs).

---

## etj_CHS2Info__X__
Where __X__ stands for integer of __1__ to __8__ specifing text position in the list.
See full list of parameters [here](/index.md#chs).

---

## etj_CHS2PosX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CHS2PosX            | any integer   | 0

Set horizontal offset of CHS2.

---

## etj_CHS2PosY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CHS2PosY            | any integer   | 0

Set vertical offset of CHS2.

---

## etj_CHSAlpha
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CHSAlpha            | 0.0 - 1.0     | 1.0

Set transparency of CHS.

---

## etj_CHSColor
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CHSColor            | [any color](/index.md#color-system) | 1.0 1.0 1.0

Set color of CHS.

---

## etj_CHSShadow
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CHSShadow           | 0 or 1        | 0

Draw shadow on CHS.

---

## etj_CHSUseFeet
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CHSUseFeet          | 0 or 1        | 0

Shift Z origin to feet level for positional calculations.

---

## etj_consoleAlpha
Name                    | values        | default
------------------------|:-------------:|-------------
etj_consoleAlpha        | 0.0 - 1.0     | 1.0

Set transparency of console. Changing requires `vid_restart`.

---

## etj_consoleColor
Name                    | values        | default
------------------------|:-------------:|-------------
etj_consoleColor        | [any color](/index.md#color-system) | 0.0 0.0 0.0

Change console background color when `etj_consoleShader` is set to __0__. Changing requires `vid_restart`.

---

## etj_consoleShader
Name                    | values        | default
------------------------|:-------------:|-------------
etj_consoleShader       | 0 or 1        | 1

Toggle console background shader. Changing requires `vid_restart`.

---

## etj_demo_freecamspeed
Name                    | values        | default
------------------------|:-------------:|-------------
etj_demo_freecamspeed   | any integer   | 800

Sets freecam movement speed in demo playback.

---

## etj_demo_rollspeed
Name                    | values        | default
------------------------|:-------------:|-------------
etj_demo_rollspeed      | any integer   | 140

Sets freecam `ROLL` turn speed in demo playback.

---

## etj_demo_pitchturnspeed
Name                    | values        | default
------------------------|:-------------:|-------------
etj_demo_pitchturnspeed | any integer   | 140

Sets freecam `PITCH` turn speed in demo playback.

---

## etj_demo_yawturnspeed
Name                    | values        | default
------------------------|:-------------:|-------------
etj_demo_yawturnspeed   | any integer   | 140

Sets freecam `YAW` turn speed in demo playback.

---

## etj_drawCGaz
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawCGaz            | 0 - 5         | 0

Draws the CGaz HUD. Has 5 [different variations](/index.md#cgaz-strafeometer) from __1__ to __5__.

---

## etj_drawCHS1
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawCHS1            | 0 or 1        | 0

Draws crosshair stats 1. [More info](/index.md#chs).

---

## etj_drawCHS2
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawCHS2            | 0 - 2         | 0

Draws crosshair stats 2. Value __2__ aligns text to the right. [More info](/index.md#chs).

---

## etj_drawClock
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawClock           | 0 - 2        | 1

Draws clock. 

* __1__ `24-hour` clock 
* __2__ `12-hour` clock

---

## etj_drawConnectionIssues
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawConnectionIssues | 0 or 1       | 1

Toggles connection interrupted text if there are connection problems. Useful for high ping players.

---

## etj_drawFoliage
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawFoliage         | 0 or 1        | 1

Draws foliage. Unlocked version of `r_drawfoliage`.

---

## etj_drawKeys
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawKeys            | 0 - 5         | 1

Draws pressed keys. There are five different keysets available:

* __1__ ETJump 1
* __2__ DeFRaG default
* __3__ ETJump 2
* __4__ ETJump 3
* __5__ Draw bound keys

---

## etj_drawLeaves
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawLeaves          | 0 or 1        | 1

Draws leaves on trees and bushes. Functionality relies on a fixed set of shaders, and only works on stock ET shaders.

---

## etj_drawMaxSpeed
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawMaxSpeed        | 0 or 1        | 0

Draws your max speed from last load.

---

## etj_drawMessageTime
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawMessageTime     | 0 - 2         | 2

Draw when a message was sent. 

* __1__ for `hours:minutes` format 
* __2__ for `hours:minutes:seconds` format.

---

## etj_drawNoJumpDelay
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawNoJumpDelay     | 0 or 1        | 0

Draw no jump delay surface detector.

Symbol shown is different depending on the maps usage of worldspawn key `nojumpdelay`.

* __ND__ when aiming at surface without jump delay while `nojumpdelay` is __0__.
* __D__ when aiming at surface with jump delay while `nojumpdelay` is __1__.

---

## etj_drawNotify
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawNotify          | 0 or 1        | 0

Draw console output on top left of screen. Unlocked version of `con_drawNotify`.

---

## etj_drawOB
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawOB              | 0 - 2         | 0

Draws overbounce meter.

* __1__ simple overbounce meter 
* __2__ don't predict sticky ob if there is an ob already or if the sticky ob detection isn't requested

Symbols meaning:

* __J__ jump ob
* __F__ fall ob
* __B__ below ob

---

## etj_drawObWatcher
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawObWatcher       | 0 or 1        | 1

Draws overbounce watcher. Allows you to save position and when you are about to hit overbounce on that surface, the detector will show `OB` without having to actually aim at the saved surface.

* `ob_save` will save your current coordinates.
* `ob_load` will load saved coordinates.
* `ob_reset` resets currently displayed coordinates so nothing will be displayed.

---

## etj_drawProneIndicator
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawProneIndicator  | 0 - 3         | 3

Draw prone area indicator.

* __1__ always draw the icon.
* __2__ only draw the icon when outside of noprone brush.
* __3__ only draw the icon when inside of noprone brush.

---

## etj_drawRunTimer
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawRunTimer        | 0 or 1        | 1

Draws the timerun timer. Doesn't draw anything if the server or map doesn't enable timeruns.

---

## etj_drawSaveIndicator

Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawSaveIndicator   | 0 - 3         | 3

Draw save area indicator.

* __1__ always draw the icon.
* __2__ only draw the icon when outside of nosave brush.
* __3__ only draw the icon when inside of nosave brush.

---

## etj_drawSimplePlayers
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawSimplePlayers   | 0 or 1        | 0

Toggles alternative drawing of other players. When enabled, a single shader is used to draw other players.

![Example](/img/etj_ghostPlayersAlt_example.png).

---

## etj_drawSlick
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawSlick           | 0 or 1        | 1

Draw slick detector. Draws `S` symbol if you are aiming at slick surface.

---

## etj_drawSnapHUD
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawSnapHUD         | 0 or 1        | 0

Draws velocity snapping HUD.

---

## etj_drawSpectatorInfo
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawSpectatorInfo   | 0 or 1        | 0

Draws a list of people spectating you.

---

## etj_drawspeed
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawspeed           | 0 - 2         | 1

Draws original ETPub-style speedometer, __2__ additionally draws max speed, that can be reset with `resetmaxspeed` command.

---

## etj_drawSpeed2
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawSpeed2          | 0 - 9         | 1

Draws ETJump speedometer under the corsshair. Has several drawing options:

* __1__ draws **current speed**
* __2__ draws **speed** and **max speed** nearby  
* __9__ displays only tens (ignores hundreds and thousands).

And several options to represent **speed** and **max speed**

* __3__ speed **^z**max
* __4__ speed **(**max**)**
* __5__ speed **^z(**max**)**
* __6__ speed **^z[**max**]**
* __7__ speed **|** max
* __8__ **Speed:** speed

---

## etj_drawTokens
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawTokens          | 0 or 1        | 1

Toggles drawing of collectible tokens.

---

## etj_enableTimeruns
Name                    | values        | default
------------------------|:-------------:|-------------
etj_enableTimeruns      | 0 or 1        | 1

Toggles timeruns. Having __0__ means don't activate any timerun timers on timerun supported map.

---

## etj_explosivesShake
Name                    | values        | default
------------------------|:-------------:|-------------
etj_explosivesShake     | 0 - 3         | 3

Controls screenshake from explosives.

* __0__ disables screenshakes
* __1__ disables for own explosives 
* __2__ disables for other player's explosives
* __3__ default behaviour

---

## etj_extraTrace
Name                    | values        | default
------------------------|:-------------:|-------------
etj_extraTrace          | bitmask       | 0

Toggles tracing of playerclips on various detectors.

* __1__ OB detector
* __2__ Slick detector
* __4__ No jump delay detector
* __8__ CHS 10-11
* __16__ CHS 12
* __32__ CHS 13-15
* __64__ CHS 16
* __128__ CHS 53

The bitmask values can be listed in console with the command `/extraTrace`.

---

## etj_fireteamAlpha
Name                    | values        | default
------------------------|:-------------:|-------------
etj_fireteamAlpha       | 0.0 - 1.0     | 1.0

Set transparency of fireteam.

---

## etj_fireteamPosX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_fireteamPosX        | any integer   | 0

Set horizontal offset of fireteam.

---

## etj_fireteamPosY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_fireteamPosY        | any integer   | 0

Set vertical offset of fireteam.

---

## etj_gunSway
Name                    | values        | default
------------------------|:-------------:|-------------
etj_gunSway             | 0 or 1        | 1

Toggles gun idle/movement sway and landing bobbing.

---

## etj_hide
Name                    | values        | default
------------------------|:-------------:|-------------
etj_hide                | 0 or 1        | 1

Toggle whether to hide other players when they get too close.

---

## etj_hideDistance
Name                    | values        | default
------------------------|:-------------:|-------------
etj_hideDistance        | any integer   | 128

How close a player has to be to be hidden from view.

---

## etj_hideFadeRange
Name                    | values        | default
------------------------|:-------------:|-------------
etj_hideFadeRange       | any integer   | 200

Additional range added to `etj_hideDistance` where other players start to fade before disappearing completely.

---

## etj_hideMe
Name                    | values        | default
------------------------|:-------------:|-------------
etj_hideMe              | 0 or 1        | 0

Hides yourself from other players view.

---

## etj_highlight
Name                    | values        | default
------------------------|:-------------:|-------------
etj_highlight           | 0 or 1        | 1

Highlights chat messages if your name was mentioned.

---

## etj_highlightSound
Name                    | values        | default
------------------------|:-------------:|-------------
etj_highlightSound      | path to .wav  | sound/world/beeper.wav

Sound that plays when your name was mentioned in the chat. Server must have the specified .wav file.

---

## etj_highlightText
Name                    | values        | default
------------------------|:-------------:|-------------
etj_highlightText       | any string    | "^3> ^z"

Prefix of the highlighted chat message.

---

## etj_HUD_chargeBar
Name                    | values        | default
------------------------|:-------------:|-------------
etj_HUD_chargeBar       | 0 or 1        | 1

Toggle chargebar.

---

## etj_HUD_fatigueBar
Name                    | values        | default
------------------------|:-------------:|-------------
etj_HUD_fatigueBar      | 0 or 1        | 1

Toggle fatigue bar.

---

## etj_HUD_fireteam
Name                    | values        | default
------------------------|:-------------:|-------------
etj_HUD_fireteam        | 0 or 1        | 1

Toggle fireteam.

---

## etj_HUD_healthBar
Name                    | values        | default
------------------------|:-------------:|-------------
etj_HUD_healthBar       | 0 or 1        | 1

Toggle health bar.

---

## etj_HUD_playerHead
Name                    | values        | default
------------------------|:-------------:|-------------
etj_HUD_playerHead      | 0 or 1        | 0

Toggle player head.

---

## etj_HUD_playerHealth
Name                    | values        | default
------------------------|:-------------:|-------------
etj_HUD_playerHealth    | 0 or 1        | 0

Toggle player health.

---

## etj_HUD_popup
Name                    | values        | default
------------------------|:-------------:|-------------
etj_HUD_popup           | 0 - 2         | 1

Enable popups. Value __2__ draws popups on right side.

---

## etj_HUD_weaponIcon
Name                    | values        | default
------------------------|:-------------:|-------------
etj_HUD_weaponIcon      | 0 or 1        | 1

Toggle weapon icon.

---

## etj_HUD_xpInfo
Name                    | values        | default
------------------------|:-------------:|-------------
etj_HUD_xpInfo          | 0 or 1        | 0

Toggle xp info.

---

## etj_itemPickupText
Name                    | values        | default
------------------------|:-------------:|-------------
etj_itemPickupText      | 0 or 1        | 1

Draw text when item is picked up.

---

## etj_keysColor
Name                    | values        | default
------------------------|:-------------:|-------------
etj_keysColor           | [any color](/index.md#color-system) | White

Set the color of pressed keys view.

---

## etj_keysShadow
Name                    | values        | default
------------------------|:-------------:|-------------
etj_keysShadow          | 0 or 1        | 0

Draw shadow on pressed keys view.

---

## etj_keysSize
Name                    | values        | default
------------------------|:-------------:|-------------
etj_keysSize            | any integer   | 48

Set the size of pressed keys view.

---

## etj_keysX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_keysX               | any integer   | 610

Set the horizontal position of pressed keys view.

---

## etj_keysY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_keysY               | any integer   | 220

Set the vertical position of pressed keys view.

---

## etj_lagometerX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_lagometerX          | any integer   | 0

Set horizontal offset of lagometer.

---

## etj_lagometerY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_lagometerY          | any integer   | 0

Set vertical offset of lagometer.

---

## etj_lightmap
Name                    | values        | default
------------------------|:-------------:|-------------
etj_lightmap            | 0-3           | 0

Draw lightmaps on surfaces that have one. Unlocked version of `r_lightmap`.

* __1__ draws regular lightmaps.
* __2__ draws temperature colored lightmaps (`vid_restart` required).
* __3__ draws inverted temperature colored lightmaps (`vid_restart` required).

---

## etj_loadviewangles
Name                    | values        | default
------------------------|:-------------:|-------------
etj_loadviewangles      | 0 or 1        | 1

Load view angles whenever you load.

---

## etj_logBanner
Name                    | values        | default
------------------------|:-------------:|-------------
etj_logBanner           | 0 or 1        | 1

Prints banner text into the console.

---

## etj_loopedSounds
Name                    | values        | default
------------------------|:-------------:|-------------
etj_loopedSounds        | 0 or 1        | 1

Enable playback of looped sounds in maps.

---

## etj_maxSpeedDuration
Name                    | values        | default
------------------------|:-------------:|-------------
etj_maxSpeedDuration    | any integer   | 2000

How long in milliseconds your max speed from last load will be visible when `etj_drawMaxSpeed` is enabled.

---

## etj_maxSpeedX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_maxSpeedX           | any integer   | 320

Horizontal location of `etj_drawMaxSpeed`.

---

## etj_maxSpeedY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_maxSpeedY           | any integer   | 320

Vertical location of `etj_drawMaxSpeed`.

---

## etj_noActivateLean
Name                    | values        | default
------------------------|:-------------:|-------------
etj_noActivateLean      | 0 or 1        | 0

Disables leaning when strafing and pressing activate in the same time.

---

## etj_noclipScale
Name                    | values        | default
------------------------|:-------------:|-------------
etj_noclipScale         | 0.1 - 20      | 1

Scales the noclip speed.

---

## etj_nofatigue
Name                    | values        | default
------------------------|:-------------:|-------------
etj_nofatigue           | 0 or 1        | 1

Toggle nofatigue.

---

## etj_noJumpDelayX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_noJumpDelayX        | any integer   | 290

Set horizontal position of no jump delay detector.

---

## etj_noJumpDelayY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_noJumpDelayY        | any integer   | 220

Set vertical position of no jump delay detector.

---

## etj_numPopups
Name                    | values        | default
------------------------|:-------------:|-------------
etj_numPopups           | 0 - 32        | 5

Maximum amount of popups to display.

---

## etj_obWatcherColor
Name                    | values        | default
------------------------|:-------------:|-------------
etj_obWatcherColor      | [any color](/index.md#color-system) | White

Set color of OB watcher.

---

## etj_obWatcherSize
Name                    | values        | default
------------------------|:-------------:|-------------
etj_obWatcherSize       | any integer   | 3

Set size of OB watcher.

---

## etj_obWatcherX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_obWatcherX          | any integer   | 100

Set horizontal position of OB watcher.

---

## etj_obWatcherY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_obWatcherY          | any integer   | 100

Set vertical position of OB watcher.

---

## etj_OBX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_OBX                 | any integer   | 320

Set horizontal position of OB detector.

---

## etj_OBY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_OBY                 | any integer   | 220

Set vertical position of OB detector.

---

## etj_offsetFactor
Name                    | values        | default
------------------------|:-------------:|-------------
etj_offsetFactor        | any integer   | -1

Set factor for `etj_offsetUnits` to control polygonOffset amount. Unlocked version of `r_offsetfactor`.

---

## etj_offsetUnits
Name                    | values        | default
------------------------|:-------------:|-------------
etj_offsetUnits         | any integer   | -2

Set distance from a shader with polygonOffset to the surface below it. Unlocked version of `r_offsetunits`.

---

## etj_onRunStart
Name                    | values        | default
------------------------|:-------------:|-------------
etj_onRunStart          | any command(s) | 

Set of commands to be executed on timerun start.

---

## etj_onRunEnd
Name                    | values        | default
------------------------|:-------------:|-------------
etj_onRunEnd            | any command(s) | 

Set of commands to be executed on timerun end.

_Note: also triggers on timerun interrupts._

---

## etj_playerOpacity
Name                    | values        | default
------------------------|:-------------:|-------------
etj_playerOpacity       | 0.0 - 1.0     | 1.0

Controls transparency level for player models. __1.0__ is fully opaque.

---

## etj_popupAlpha
Name                    | values        | default
------------------------|:-------------:|-------------
etj_popupAlpha         | 0.0 - 1.0     | 1.0

Set transparency of popups.

---

## etj_popupFadeTime
Name                    | values        | default
------------------------|:-------------:|-------------
etj_popupFadeTime       | any integer   | 2500

How long in milliseconds it takes for a popup to fade.

---

## etj_popupGrouped
Name                    | values        | default
------------------------|:-------------:|-------------
etj_popupGrouped        | 0 - 2         | 1

Groups identical repetitive popup messages into one.

* __1__ group popups, print duplicates in console.
* __2__ group popups and console prints.

---

## etj_popupPosX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_popupPosX           | any integer   | 0

Set horizontal offset of popups.

---

## etj_popupPosY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_popupPosY           | any integer   | 0

Set vertical offset of popups.

---

## etj_popupShadow
Name                    | values        | default
------------------------|:-------------:|-------------
etj_popupShadow         | 0 or 1        | 0

Draw shadow on popups.

---

## etj_popupStayTime
Name                    | values        | default
------------------------|:-------------:|-------------
etj_popupStayTime       | any integer   | 2000

How long in milliseconds it takes for a popup to start fading.

---

## etj_popupTime
Name                    | values        | default
------------------------|:-------------:|-------------
etj_popupTime           | any integer   | 1000

How long it takes for a popup to show on the sidebar in milliseconds.

---

## etj_predefineddemokeys
Name                    | values        | default
------------------------|:-------------:|-------------
etj_predefineddemokeys  | 0 or 1        | 1

Use predefined demo keybindings in demo playback.

---

## etj_proneIndicatorX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_proneindicatorX     | any integer   | 615

Set horizontal position of prone area indicator.

---

## etj_proneIndicatorY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_proneindicatorY     | any integer   | 338

Set vertical position of prone area indicator.

---

## etj_quickFollow
Name                    | values        | default
------------------------|:-------------:|-------------
etj_quickFollow         | 0 - 2         | 2

Spectate players by aiming at them and pressing `+activate`

* __1__ enables quick follow.
* __2__ additionally draws a hint under player name.

---

## etj_realFov
Name                    | values        | default
------------------------|:-------------:|-------------
etj_realFov             | 0 or 1        | 0

Takes aspect ratio into account when calculating FOV. Enabling results in higher FOV on widescreen aspect ratio.

---

## etj_runTimerAutoHide
Name                    | values        | default
------------------------|:-------------:|-------------
etj_runTimerAutoHide    | 0 or 1        | 1

Automatically hides run timer if it's not being used.

---

## etj_runTimerInactiveColor
Name                    | values        | default
------------------------|:-------------:|-------------
etj_runTimerInactiveColor | [any color](/index.md#color-system) | mdgrey

Set color of timerun timer when no timerun is active.

---

## etj_runTimerShadow
Name                    | values        | default
------------------------|:-------------:|-------------
etj_runTimerShadow      | 0 or 1        | 0

Toggles shadow under the run timer.

---

## etj_runTimerX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_runTimerX           | any integer   | 320

Changes run timer's horizontal position.

---

## etj_runTimerY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_runTimerY           | any integer   | 380

Changes run timer's vertical position.

---

## etj_saveIndicatorX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_saveIndicatorX      | any integer   | 615

Set horizontal position of save zone indicator.

---

## etj_saveIndicatorY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_saveIndicatorY      | any integer   | 363

Set vertical position of save zone indicator.

---

## etj_showTris
Name                    | values        | default
------------------------|:-------------:|-------------
etj_showTris            | 0 - 2           | 0

Draws edges of triangles. Unlocked version of `r_showTris`.

* __1__ draws triangle edges on your current POV.
* __2__ draws triangle edges on your current PVS.

---

## etj_simplePlayersColor
Name                    | values        | default
------------------------|:-------------:|-------------
etj_simplePlayersColor  | [any color](/index.md#color-system) | 1.0 1.0 1.0

Changes player color when `etj_ghostPlayersAlt` is enabled.

---

## etj_slickX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_slickX              | any integer   | 315

Changes slick detector's horizontal position.

---

## etj_slickY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_slickY              | any integer   | 220

Changes slick detector's vertical position.

---

## etj_snapHUDColor1
Name                    | values        | default
------------------------|:-------------:|-------------
etj_snapHUDColor1       | [any color](/index.md#color-system)   | 0.0 1.0 1.0 0.75

Sets the primary color of velocity snapping HUD.

---

## etj_snapHUDColor2
Name                    | values        | default
------------------------|:-------------:|-------------
etj_snapHUDColor2       | [any color](/index.md#color-system)   | 0.0 1.0 1.0 0.75

Sets the secondary color of velocity snapping HUD.

---

## etj_snapHUDFov
Name                    | values        | default
------------------------|:-------------:|-------------
etj_snapHUDColor2       | 0 - 180       | 0

Sets the FOV of the velocity snapping HUD. __0__ means use your current in-game FOV.

---

## etj_snapHUDHeight
Name                    | values        | default
------------------------|:-------------:|-------------
etj_snapHUDHeight       | any integer   | 10

Changes the height of the velocity snapping HUD.

---

## etj_snapHUDOffsetY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_snapHUDHeight       | any integer   | 0

Changes Y-axis position of the velocity snapping HUD.

---

## etj_spectatorInfoX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_spectatorInfoX      | any integer   | 320

Changes horizontal position of the list of people spectating you.

---

## etj_spectatorInfoY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_spectatorInfoY      | any integer   | 40

Changes vectical position of the list of people spectating you.

---

## etj_speedAlpha
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedAlpha          | 0.0 - 1.0     | 1.0

Controls ETJump speedometer transparency.

---

## etj_speedColor
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedColor          | [any color](/index.md#color-system) | White

Sets ETJump speedometer color.

---

## etj_speedColorUsesAccel
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedColorUsesAccel | 0 or 1        | 0

Changes ETJump speedometer color to represent acceleration or deceleration.

---

## etj_speedinterval
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedinterval       | any integer   | 100

How often speedometer 1 gets updated in milliseconds.

---

## etj_speeds
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speeds              | 0 - 7         | 0

Output render statistics to console. Unlocked version of `r_speeds`.

Different values output following information:

* __1__ surfaces (always shown)
* __2__ culling
* __3__ viewcluster
* __4__ dlights
* __5__ render distance
* __6__ flares
* __7__ decals

---

## etj_speedShadow
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedShadow         | 0 or 1        | 0

Toggles shadow under the ETJump speedometer.

---

## etj_speedSize
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedSize           | any integer   | 3

Set size of the ETJump speedometer.

---

## etj_speedunit
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedunit           | 0 - 2         | 0

Speedometer 1 speed measure units. 

* __0__ for UPS 
* __1__ for MPH
* __2__ for KPH

---

## etj_speedX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedX              | any integer   | 320

Horizontal position of the ETJump speedometer.

---

## etj_speedXYonly
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedXYonly         | 0 or 1        | 1

Disables vertical speed from speedometer 1.

---

## etj_speedY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedY              | any integer   | 360

Vertical position of the ETJump speedometer.

---

## etj_stretchCgaz
Name                    | values        | default
------------------------|:-------------:|-------------
etj_stretchCgaz         | 0 or 1        | 1

Stretches CGaz when using widescreen aspect ratio.

---

## etj_touchPickupWeapons
Name                    | values        | default
------------------------|:-------------:|-------------
etj_touchPickupWeapons  | 0 - 2         | 0

Automatically pick up weapons by touching them.

* __1__ only picks up weapons dropped by you or spawned in map.
* __2__ picks up all weapons.

_Note: this cvar has no effect unless `cg_autoactivate` is set to __1__._

---

## etj_uphillSteps
Name                    | values        | default
------------------------|:-------------:|-------------
etj_uphillSteps         | 0 or 1        | 1

Play footsteps on very low landing speeds.

---

## etj_viewlog
Name                    | values        | default
------------------------|:-------------:|-------------
etj_viewlog             | 0 or 1        | 1

Toggles an external console window, mainly used for copy pasting etc. Unlocked version of `viewlog`.

---

## etj_viewPlayerPortals
Name                    | values        | default
------------------------|:-------------:|-------------
etj_viewPlayerPortals   | 0 - 2         | 1

Toggles other players portals. 

* __0__ don't show
* __1__ always show
* __2__ show when spectating

---

## etj_weaponSound
Name                    | values        | default
------------------------|:-------------:|-------------
etj_weaponSound         | 0 or 1        | 1

Play weapon sound when firing a weapon.

---

## etj_wolfFog
Name                    | values        | default
------------------------|:-------------:|-------------
etj_wolfFog             | 0 or 1        | 1

Draws fog. Unlocked version of `r_wolffog`.

---

## etj_zFar
Name                    | values        | default
------------------------|:-------------:|-------------
etj_zFar                | any integer   | 0

Set draw distance. Setting this to __0__ uses maps `farplanedist` value. Unlocked version of `r_zfar`.

---

## movie_changeFovBasedOnSpeed
Name                    | values        | default
------------------------|:-------------:|-------------
movie_changeFovBasedOnSpeed |0 or 1     | 0

Toggles adjusting FOV based on speed.

---

## movie_fovIncreasePerFrame
Name                    | values        | default
------------------------|:-------------:|-------------
movie_fovIncreasePerFrame | any integer | 1

How many units FOV should change per frame.

----

## movie_fovMax
Name                    | values        | default
------------------------|:-------------:|-------------
movie_fovMax            | any integer   | 140

Maximum value FOV can increase to.

_Note: values outside of __90-160__ require `developer 1`._

---

## movie_fovMaxSpeed
Name                    | values        | default
------------------------|:-------------:|-------------
movie_fovMaxSpeed       | any integer   | 1200

UPS value at which maximum FOV is reached.

---

## movie_fovMin
Name                    | values        | default
------------------------|:-------------:|-------------
movie_fovMin            | any integer   | 90

Minimum value FOV can decrease to.

_Note: values outside of __90-160__ require `developer 1`._

---

## movie_fovMinSpeed
Name                    | values        | default
------------------------|:-------------:|-------------
movie_fovMinSpeed       | any integer   | 400

UPS value at which minimum FOV is reached.

---
