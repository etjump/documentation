# List of ETJump client cvars
Below is a list of all ETJump related cvars (console variables) available for players.

---

## b_demo_lookat
Name                    | values        | default
------------------------|:-------------:|-------------
b_demo_lookat           | any integer   | -1

Specifies an entity to focus freecam at on demo playback. **-1** disables focus.

_Note: this cvar shares it's name with the ETPro variant for Camtrace 3D compatibility._

---

## etj_accelAlign
Name                    | values        | default
------------------------|:-------------:|-------------
etj_accelAlign          | 0 - 2         | 0

Set the alignment acceleration meter.

* **0** Center
* **1** Left align
* **2** Right align

---

## etj_accelAlpha
Name                    | values        | default
------------------------|:-------------:|-------------
etj_accelAlpha          | 0.0 - 1.0     | 1.0

Sets alpha of acceleration meter.

---

## etj_accelColor
Name                    | values                                | default
------------------------|:-------------------------------------:|-------------
etj_accelColor          | [any color](../index.md#color-system) | white

Sets color of acceleration meter.

_Note: use [`etj_accelAlpha`](etjump_cvars.md/#etj_accelalpha) to set alpha._

---

## etj_accelColorUsesAccel
Name                    | values        | default
------------------------|:-------------:|-------------
etj_accelColorUsesAccel | 0 - 2         | 0

Changes acceleration meter color to represent acceleration or deceleration.

* **1** simple, green if accelerating, red if decelerating, white if no input
* **2** advanced, takes into account per vector and current movement direction
    * green - optimal acceleration
    * yellow - suboptimal acceleration relative to movement direction
    * red - no acceleration towards movement direction
    * white - no input

_Note: due to inaccuracies in interpolation, advanced coloring is disabled while spectating and in demo playback, and simple acceleration coloring is used instead._

---

## etj_accelShadow
Name                    | values        | default
------------------------|:-------------:|-------------
etj_accelShadow         | 0 or 1        | 1

Toggle shadow on acceleration meter.

---

## etj_accelSize
Name                    | values        | default
------------------------|:-------------:|-------------
etj_accelSize           | any value     | 3

Sets size of acceleration meter.

---

## etj_accelX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_accelSize           | any value     | 320

Sets X position of acceleration meter.

---

## etj_accelY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_accelSize           | any value     | 340

Sets Y position of acceleration meter.

---

## etj_ad_savePBOnly
Name                    | values        | default
------------------------|:-------------:|-------------
etj_ad_savePBOnly       | 0 or 1        | 0

Whether or not autodemo should save a demo when finishing a timerun.

* **0** save all demos.
* **1** save only personal bests.

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

## etj_altScoreboard
Name                    | values        | default
------------------------|:-------------:|-------------
etj_altScoreboard       | 0 - 3         | 0

Changes the scoreboard to an alternative one.  

* **0** default ETMain styled scoreboard.
* **1** and **2** draw alternatively styled scoreboard.
* **3** draws a compact scoreboard with dynamic size and position adjustments.

---

## etj_autoDemo
Name                    | values        | default
------------------------|:-------------:|-------------
etj_autoDemo            | 0 - 2         | 0

Automatically start recording a demo whenever player loads (unless a timerun is active) or spawns.

* **1** enabled only for maps with a timerun.
* **2** enabled for all maps.

_Note: Autodemo will keep a maximum of 20 temp demos, located in `demos/temp` before it starts overwriting them._

---

## etj_autoLoad
Name                    | values        | default
------------------------|:-------------:|-------------
etj_autoLoad            | 0 or 1        | 1

Automatically load into last saved position when joining a team.

---

## etj_autoPortalBinds
Name                    | values        | default
------------------------|:-------------:|-------------
etj_autoPortalBinds     | 0 or 1        | 1

Automatically bind `+attack2` to `weapalt` key and back when equipping/unequipping portal gun.

---

## etj_CGaz1Color1
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGaz1Color1         | [any color](../index.md#color-system) | 0.75 0.75 0.75 0.75

Sets the no accel zone color of CGaz HUD **1**.

---

## etj_CGaz1Color2
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGaz1Color2         | [any color](../index.md#color-system) | 0.0 1.0 0.0 0.75

Sets the minimum angle color of CGaz HUD **1**.

---

## etj_CGaz1Color3
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGaz1Color3         | [any color](../index.md#color-system) | 0.0 0.2 0.0 0.75

Sets the accel zone color of CGaz HUD **1**.

---

## etj_CGaz1Color4
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGaz1Color4         | [any color](../index.md#color-system) | 1.0 1.0 0.0 0.75

Sets the max angle color of CGaz HUD **1**.

---

## etj_CGaz1DrawSnapZone
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGaz1DrawSnapZone   | 0 or 1        | 0

Extends minline drawing on CGaz 1 to the end of the current snap zone.

---

## etj_CGaz2Color1
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGaz2Color1          | [any color](../index.md#color-system) | 1.0 0.0 0.0 1.0

Set the primary color of CGaz HUD **2**.

---

## etj_CGaz2Color2
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGaz2Color2          | [any color](../index.md#color-system) | 0.0 1.0 1.0 1.0

Set the secondary color of CGaz HUD **2**.

---

## etj_CGaz2FixedSpeed
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGaz2FixedSpeed     | 0 - 1200      | 0

When set to higher than **0**, CGaz 2 will be drawn as if the player had the set amount of speed, instead of being adjusted by players real speed.

---

## etj_CGaz2NoVelocityDir
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGaz2NoVelocityDir  | 0 - 2         | 0

Controls drawing of velocity direction line on CGaz 2.

* **1** never draw velocity direction line
* **2** draw only while under wishspeed

---

## etj_CGazFov
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGazFov             | 0 - 179       | 0

Sets the FOV of CGaz HUD **1**. **0** means use your current in-game FOV.

---

## etj_CGazHeight
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGazHeight          | any integer   | 20

Height of the CGaz HUD **1**.

---

## etj_CGazOnTop
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGazOnTop           | 0 or 1        | 0

Toggles drawing of CGaz HUD on top of Snaphud.

---

## etj_CGazTrueness
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGazTrueness        | bitflag       | 2

Set "trueness" flags on CGaz HUD.

* **1** Show upmove influence
* **2** Show true groundzones (CGaz 1 only)

---

## etj_CGazY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGazY               | any integer   | 240

Vertical position of CGaz HUD **1**.

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

## etj_checkpointsCount
Name                    | values        | default
------------------------|:-------------:|-------------
etj_checkpointsCount    | 1-5           | 3

How many checkpoints timers to draw.

---

## etj_checkpointsPopup
Name                    | values        | default
------------------------|:-------------:|-------------
etj_checkpointsPopup    | 0 or 1        | 1

Toggle checkpoint popup on screen when hitting a checkpoint.

_Note: This does not require the regular checkpoint timer to be visible._

---

## etj_checkpointsPopupDuration
Name                         | values        | default
-----------------------------|:-------------:|-------------
etj_checkpointsPopupDuration | any integer   | 1000

How long in milliseconds the checkpoint popup stays on screen.

---

## etj_checkpointsPopupSize
Name                     | values        | default
-------------------------|:-------------:|-------------
etj_checkpointsPopupSize | any value     | 2

Sets the size of the checkpoint popup.

---

## etj_checkpointsPopupShadow
Name                       | values        | default
---------------------------|:-------------:|-------------
etj_checkpointsPopupShadow | 0 or 1        | 1

Draw shadow on checkpoint popup.

---

## etj_checkpointsPopupX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_checkpointsPopupX   | any value     | 320

Sets X position of checkpoint popup.

---

## etj_checkpointsPopupY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_checkpointsPopupY   | any value     | 200

Sets Y position of checkpoint popup.

---

## etj_checkpointsShadow
Name                    | values        | default
------------------------|:-------------:|-------------
etj_checkpointsShadow   | 0 or 1        | 1

Draw shadow on checkpoint timer.

---

## etj_checkpointsSize
Name                    | values        | default
------------------------|:-------------:|-------------
etj_checkpointsSize     | any value     | 2

Sets the size of checkpoint timer.

---

## etj_checkpointsStyle
Name                    | values        | default
------------------------|:-------------:|-------------
etj_checkpointsStyle    | 0 or 1        | 0

Sets the style of checkpoint timer.

* **0** relative time
* **1** absolute time

---

## etj_checkpointsX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_checkpointsSizeX    | any value     | 320

Sets the X position of checkpoint timer.

_Note: Checkpoint timer must be in detached mode (`etj_drawCheckpoints 2`) to adjust the position._

---

## etj_checkpointsY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_checkpointsSizeY    | any value     | 380

Sets the Y position of checkpoint timer.

_Note: Checkpoint timer must be in detached mode (`etj_drawCheckpoints 2`) to adjust the position._

---

## etj_CHS1Info**X**
Where **X** stands for integer of **1** to **8** specifing text position on the circle.
See full list of parameters [here](../index.md#chs).

---

## etj_CHS2Info**X**
Where **X** stands for integer of **1** to **8** specifing text position in the list.
See full list of parameters [here](../index.md#chs).

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
etj_CHSColor            | [any color](../index.md#color-system) | 1.0 1.0 1.0

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

## etj_clear
Name                    | values        | default
------------------------|:-------------:|-------------
etj_clear               | 0 or 1        | 0

Force screen clear with pink color when drawing void. Unlocked version of `r_clear`.

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
etj_consoleColor        | [any color](../index.md#color-system) | 0.0 0.0 0.0

Change console background color when `etj_consoleShader` is set to **0**. Changing requires `vid_restart`.

---

## etj_consoleShader
Name                    | values        | default
------------------------|:-------------:|-------------
etj_consoleShader       | 0 or 1        | 1

Toggle console background shader. Changing requires `vid_restart`.

---

## etj_crosshairOutline
Name                    | values        | default
------------------------|:-------------:|-------------
etj_crosshairOutline    | 0 or 1        | 1

Toggles drawing of outline on ETJump crosshairs.

---

## etj_crosshairScaleX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_crosshairScaleX     | -5 - 5        | 1.0

Sets horizontal scaling of crosshair.

---

## etj_crosshairScaleY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_crosshairScaleY     | -5 - 5        | 1.0

Sets vertical scaling of crosshair.

---

## etj_crosshairThickness
Name                    | values        | default
------------------------|:-------------:|-------------
etj_crosshairThickness  | 0 - 5         | 1.0

Sets line thickness of ETJump crosshairs.

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

## etj_drawAccel
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawAccel           | 0 or 1        | 0

Toggle drawing of acceleration values on x/y axes.

---

## etj_drawBanners
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawBanners         | 0 or 1        | 1

Toggle drawing of banner prints.

---

## etj_drawCGaz
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawCGaz            | bitflag       | 0

Draws the CGaz HUD. Has 2 [different variations](../index.md#cgaz-strafeometer).

---

## etj_drawCheckpoints
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawCheckpoints     | 0 - 2        | 1

Draws checkpoint timer.

* **1** below runtimer 
* **2** detached

---

## etj_drawCHS1
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawCHS1            | 0 or 1        | 0

Draws crosshair stats 1. [More info](../index.md#chs).

---

## etj_drawCHS2
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawCHS2            | 0 - 2         | 0

Draws crosshair stats 2. Value **2** aligns text to the right. [More info](../index.md#chs).

---

## etj_drawClips
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawClips           | 0 or 1        | 0

Toggle clip brush drawing. Unlocked version of `r_drawClips`. Requires [ETe client](https://github.com/etfdevs/ETe) release from Sep 10th 2022 or newer. [More info](../index.md#clip-trigger-slick-drawing).

---

## etj_drawClock
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawClock           | 0 - 2        | 1

Draws clock. 

* **1** `24-hour` clock 
* **2** `12-hour` clock

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

## etj_drawJumpSpeeds
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawJumpSpeeds      | 0 or 1        | 1

Draws last 10 jump speeds.

---

## etj_drawKeys
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawKeys            | 0 - 5         | 1

Draws pressed keys. There are five different keysets available:

* **1** ETJump 1
* **2** DeFRaG default
* **3** ETJump 2
* **4** ETJump 3
* **5** Draw bound keys

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

* **1** for `hours:minutes` format 
* **2** for `hours:minutes:seconds` format.

---

## etj_drawNoclipIndicator
Name                     | values        | default
-------------------------|:-------------:|-------------
etj_drawNoclipIndicator  | 0 - 3         | 3

Draw no-noclip area indicator.

* **1** always draw the icon.
* **2** only draw the icon when outside of no-noclip brush.
* **3** only draw the icon when inside of no-noclip brush.

---

## etj_drawNoJumpDelay
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawNoJumpDelay     | 0 or 1        | 0

Draw no jump delay surface detector.

Symbol shown is different depending on the maps usage of worldspawn key `nojumpdelay`.

* **ND** when aiming at surface without jump delay while `nojumpdelay` is **0**.
* **D** when aiming at surface with jump delay while `nojumpdelay` is **1**.

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

* **1** simple overbounce meter 
* **2** predict sticky overbounces

Symbols meaning:

* **J** jump ob
* **F** fall ob
* **B** below ob
* **S** sticky ob

_Note: sticky overbounces are never drawn on surfaces that are on the exact same height as you are currently, as it is always possible to get a sticky OB in such cases, and drawing it would mostly just be distracting._

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

* **1** always draw the icon.
* **2** only draw the icon when outside of noprone brush.
* **3** only draw the icon when inside of noprone brush.

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

* **1** always draw the icon.
* **2** only draw the icon when outside of nosave brush.
* **3** only draw the icon when inside of nosave brush.

---

## etj_drawScoreboardInactivity

Name                         | values        | default
-----------------------------|:-------------:|-------------
etj_drawScoreboardInactivity | 0 or 1        | 1

Draw an idle indicator on scoreboard for clients who haven't registered an input for **3** minutes.

---

## etj_drawSimplePlayers
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawSimplePlayers   | 0 or 1        | 0

Toggles alternative drawing of other players. When enabled, a single shader is used to draw other players.

![Example](../img/etj_ghostPlayersAlt_example.png).

---

## etj_drawSlick
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawSlick           | 0 or 1        | 1

Draw slick detector. Draws `S` symbol if you are aiming at slick surface.

---

## etj_drawSlicks
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawSlicks          | 0 or 1        | 0

Toggle slick surface drawing. Works for surfaces with `surfaceparm slick` and angle slicks. Unlocked version of `r_drawSlicks`. Requires [ETe client](https://github.com/etfdevs/ETe) release from Sep 10th 2022 or newer. [More info](../index.md#clip-trigger-slick-drawing).

---

## etj_drawSnapHUD
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawSnapHUD         | 0 - 2         | 0

Draws velocity snapping HUD.

* **1** Draw full snapzones
* **2** Draw only edges of snapzones

---

## etj_drawSpectatorInfo
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawSpectatorInfo   | 0 - 3         | 0

Draws a list of people spectating you. Idle spectators are drawn with sligtly transparent colors.

* **1** Left aligned
* **2** Center aligned
* **3** Right aligned

---

## etj_drawspeed
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawspeed           | 0 - 2         | 1

Draws original ETPub-style speedometer, **2** additionally draws max speed, that can be reset with `resetmaxspeed` command.

* **1** draw speed
* **2** draw speed + maxspeed

---

## etj_drawSpeed2
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawSpeed2          | 0 - 9         | 1

Draws ETJump speedometer under the corsshair. Has several drawing options:

* **1** draws **current speed**
* **2** draws **speed** and **max speed** nearby  
* **9** displays only tens (ignores hundreds and thousands).

And several options to represent **speed** and **max speed**

* **3** speed **^z**max
* **4** speed **(**max**)**
* **5** speed **^z(**max**)**
* **6** speed **^z[**max**]**
* **7** speed **|** max
* **8** **Speed:** speed

---

## etj_drawStrafeQuality
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawStrafeQuality   | 0 or 1        | 0

Toggles drawing of strafe quality meter.

---

## etj_drawTokens
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawTokens          | 0 or 1        | 1

Toggles drawing of collectible tokens.

---

## etj_drawTriggers
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawTriggers        | 0 or 1        | 0

Toggle trigger brush drawing. Unlocked version of `r_drawTriggers`. Requires [ETe client](https://github.com/etfdevs/ETe) release from Sep 10th 2022 or newer. [More info](../index.md#clip-trigger-slick-drawing).

---

## etj_drawUpmoveMeter
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawUpmoveMeter     | bitflag       | 0

Draws upmove meter.

* **0** Off
* **1** Graph
* **2** Text

---

## etj_enableTimeruns
Name                    | values        | default
------------------------|:-------------:|-------------
etj_enableTimeruns      | 0 or 1        | 1

Toggles timeruns. Having **0** means don't activate any timerun timers on timerun supported map.

---

## etj_expandedMapAlpha
Name                    | values        | default
------------------------|:-------------:|-------------
etj_expandedMapAlpha    | 0.0 - 1.0     | 0.7

Set transparency of expanded command map (`+mapexpand`).

---

## etj_explosivesShake
Name                    | values        | default
------------------------|:-------------:|-------------
etj_explosivesShake     | 0 - 3         | 3

Controls screenshake from explosives.

* **0** disables screenshakes
* **1** disables for own explosives 
* **2** disables for other player's explosives
* **3** default behaviour

---

## etj_extraTrace
Name                    | values        | default
------------------------|:-------------:|-------------
etj_extraTrace          | bitflags      | 0

Toggles tracing of playerclips on various detectors.

* **1** OB detector
* **2** Slick detector
* **4** No jump delay detector
* **8** CHS 10-11
* **16** CHS 12
* **32** CHS 13-15
* **64** CHS 16
* **128** CHS 53

The bitflags values can be listed in console with the command `/extraTrace`.

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

## etj_fixedCompassShader
Name                    | values        | default
------------------------|:-------------:|-------------
etj_fixedCompassShader  | 0 or 1        | 0

Toggle overriding the shader used for compass in the map with a fixed, default shader which ensures that the corners of the compass will be correctly cropped. Original image is still used for drawing. This is mostly unnoticeable when enabled, but since it overrides the shader, it will break certain special command map shaders, such as the animated compass of Skacharohuth.

---

## etj_fixedCushionSteps
Name                    | values        | default
------------------------|:-------------:|-------------
etj_fixedCushionSteps   | 0 or 1        | 0

Toggles playing correct step sounds when landing on a cushion brush.

---

## etj_flareSize
Name                    | values        | default
------------------------|:-------------:|-------------
etj_flareSize           | any value     | 40

Sets the size of flares and coronas. Unlocked version of `r_flareSize`.

---

## etj_foostepVolume
Name                    | values        | default
------------------------|:-------------:|-------------
etj_foostepVolume       | any value     | 1.0

Scales the volume of footsteps and landing sounds.

---

## etj_FPSMeterUpdateInterval
Name                       | values        | default
---------------------------|:-------------:|-------------
etj_FPSMeterUpdateInterval | any integer   | 250

Sets the update interval of FPS meter in milliseconds.

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

Toggles drawing of popup messages.

* **1** draw left-aligned
* **2** draw right-aligned

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

## etj_jumpSpeedsColor
Name                    | values        | default
------------------------|:-------------:|-------------
etj_jumpSpeedsColor     | [any color](../index.md#color-system) | 1.0 1.0 1.0 1.0

Set the color of jump speeds display. Also used as a color for label text.

_Note: When `etj_jumpSpeedsShowDiff` is enabled, this color will be used for jumps that are equal speed to previous one._

---

## etj_jumpSpeedsFasterColor
Name                      | values        | default
--------------------------|:-------------:|-------------
etj_jumpSpeedsFasterColor | [any color](../index.md#color-system) | 0.0 1.0 0.0 1.0

Set the color to use for a jump that was faster than previous jump on jump speeds display.

---

## etj_jumpSpeedsMinSpeed
Name                      | values        | default
--------------------------|:-------------:|-------------
etj_jumpSpeedsMinSpeed    | any integer   | 0

When set to higher than **0**, any jump slower than the set value will be colored with `etj_jumpSpeedsSlowerColor`. Works independently of `etj_jumpSpeedsShowDiff`.

---

## etj_jumpSpeedsShadow
Name                      | values        | default
--------------------------|:-------------:|-------------
etj_jumpSpeedsShadow      | 0 or 1        | 1

Draw shadow on jump speeds display.

---

## etj_jumpSpeedsShowDiff
Name                      | values        | default
--------------------------|:-------------:|-------------
etj_jumpSpeedsShowDiff    | 0 or 1        | 0

Toggle coloring jump speeds with `etj_jumpSpeedsFasterColor`/`etj_jumpSpeedsSlowerColor` depending on if a jump was faster or slower than previous one.

---

## etj_jumpSpeedsSlowerColor
Name                      | values        | default
--------------------------|:-------------:|-------------
etj_jumpSpeedsSlowerColor | [any color](../index.md#color-system) | 1.0 0.0 0.0 1.0

Set the color to use for a jump that was slower than previous jump on jump speeds display.

---

## etj_jumpSpeedsStyle
Name                      | values        | default
--------------------------|:-------------:|-------------
etj_jumpSpeedsStyle       | bitflag       | 0

Set various drawing options for jump speeds display.

* **1** draw horizontal list
* **2** hide label text
* **4** reversed list (latest jump first)

---

## etj_jumpSpeedsX
Name                      | values        | default
--------------------------|:-------------:|-------------
etj_jumpSpeedsX           | any value     | 0

X offset of jump speeds display.

---

## etj_jumpSpeedsY
Name                      | values        | default
--------------------------|:-------------:|-------------
etj_jumpSpeedsX           | any value     | 0

Y offset of jump speeds display.

---

## etj_keysColor
Name                    | values        | default
------------------------|:-------------:|-------------
etj_keysColor           | [any color](../index.md#color-system) | White

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

* **1** draws regular lightmaps.
* **2** draws temperature colored lightmaps (`vid_restart` required).
* **3** draws inverted temperature colored lightmaps (`vid_restart` required).

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
etj_maxSpeedY           | any integer   | 300

Vertical location of `etj_drawMaxSpeed`.

---

## etj_menuSensitivity
Name                    | values        | default
------------------------|:-------------:|-------------
etj_menuSensitivity     | any value     | 1.0

Sets mouse sensitivity for menus.

---

## etj_muzzleFlash
Name                    | values        | default
------------------------|:-------------:|-------------
etj_muzzleFlash         | 0 - 3         | 1

Controls muzzleflash drawing.

* **1** always draw
* **2** draw only for other players
* **3** draw only for yourself

---

## etj_noActivateLean
Name                    | values        | default
------------------------|:-------------:|-------------
etj_noActivateLean      | 0 or 1        | 0

Disables leaning when strafing and pressing `+activate` at the same time.

---

## etj_noclipIndicatorX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_noclipIndicatorX    | any value     | 615

Sets X position of no-noclip indicator.

---

## etj_noclipIndicatorY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_noclipIndicatorY    | any value     | 313

Sets Y position of no-noclip indicator.

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

## etj_noPanzerAutoswitch
Name                    | values        | default
------------------------|:-------------:|-------------
etj_noPanzerAutoswitch  | 0 or 1        | 0

Toggle automatic weapon switch after firing a panzerfaust.

_Note: autoswitch will occur when completely out of ammo regardless of this._

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
etj_obWatcherColor      | [any color](../index.md#color-system) | White

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

Set factor for `etj_offsetUnits` to control `polygonOffset` amount. Unlocked version of `r_offsetfactor`.

---

## etj_offsetUnits
Name                    | values        | default
------------------------|:-------------:|-------------
etj_offsetUnits         | any integer   | -2

Set distance from a shader with `polygonOffset` to the surface below it. Unlocked version of `r_offsetunits`.

---

## etj_onRunStart
Name                    | values        | default
------------------------|:-------------:|-------------
etj_onRunStart          | any text      | 

Set of commands to be executed on timerun start.

---

## etj_onRunEnd
Name                    | values        | default
------------------------|:-------------:|-------------
etj_onRunEnd            | any text      | 

Set of commands to be executed on timerun end.

_Note: also triggers on timerun interrupts._

---

## etj_optimizePrediction
Name                    | values        | default
------------------------|:-------------:|-------------
etj_optimizePrediction  | 0 or 1        | 1

Enables optimized playerstate prediction for improved playerstate prediction performance.

---

## etj_playerOpacity
Name                    | values        | default
------------------------|:-------------:|-------------
etj_playerOpacity       | 0.0 - 1.0     | 1.0

Controls transparency level for player models. **1.0** is fully opaque.

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

* **1** group popups, print duplicates in console.
* **2** group popups and console prints.

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

## etj_projection
Name                    | values        | default
------------------------|:-------------:|-------------
etj_projection          | 0 - 2         | 0

Set projection type used for CGaz **1** and SnapHUD.

* **0** rectilinear
* **1** cylindrical
* **2** panini

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

* **1** enables quick follow.
* **2** additionally draws a hint under player name.

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
etj_runTimerInactiveColor | [any color](../index.md#color-system) | mdgrey

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

## etj_saveMsg
Name                    | values        | default
------------------------|:-------------:|-------------
etj_saveMsg             | any string    | ^7Saved

Set the message to display when using `save`.

---

## etj_showTris
Name                    | values        | default
------------------------|:-------------:|-------------
etj_showTris            | 0 - 2         | 0

Draws edges of triangles. Unlocked version of `r_showTris`. Functionality varies slightly depending on engine used.

#### ET 2.60b
* **1** draws triangle edges on your current POV.
* **2** draws triangle edges on your current PVS.

#### ET: Legacy
* Same as **ET 2.60b**, except 2D elements are ignored (e.g. HUD).

#### ETe
* **1** draws triangle edges, excluding 2D elements.
* **2** draws triangle edges, including 2D elements.
* `r_trisMode` is used to toggle between POV/PVS drawing.

---

## etj_simplePlayersColor
Name                    | values        | default
------------------------|:-------------:|-------------
etj_simplePlayersColor  | [any color](../index.md#color-system) | 1.0 1.0 1.0

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

## etj_snapHUDActiveIsPrimary
Name                       | values        | default
---------------------------|:-------------:|-------------
etj_snapHUDActiveIsPrimary | 0 or 1        | 0

Toggles snaphud colors so that the zone you are aiming at will always be drawn with primary color.

---

## etj_snapHUDColor1
Name                    | values        | default
------------------------|:-------------:|-------------
etj_snapHUDColor1       | [any color](../index.md#color-system) | 0.0 1.0 1.0 0.75

Sets the primary color of velocity snapping HUD.

---

## etj_snapHUDColor2
Name                    | values        | default
------------------------|:-------------:|-------------
etj_snapHUDColor2       | [any color](../index.md#color-system) | 0.05 0.05 0.05 0.1

Sets the secondary color of velocity snapping HUD.

---

## etj_snapHUDEdgeThickness
Name                     | values        | default
-------------------------|:-------------:|-------------
etj_snapHUDEdgeThickness | 1 - 128       | 10

Thickness of snaphud edges when [`etj_drawSnapHUD`](etjump_cvars.md/#etj_drawsnaphud) is set to **2**.

---

## etj_snapHUDFov
Name                    | values        | default
------------------------|:-------------:|-------------
etj_snapHUDColor2       | 0 - 180       | 0

Sets the FOV of the velocity snapping HUD. **0** means use your current in-game FOV.

---

## etj_snapHUDHeight
Name                    | values        | default
------------------------|:-------------:|-------------
etj_snapHUDHeight       | any integer   | 10

Changes the height of the velocity snapping HUD.

---

## etj_snapHUDHLActive
Name                    | values        | default
------------------------|:-------------:|-------------
etj_snapHUDHLActive     | 0 or 1        | 0

Highlights currently active snapzone with a different color.

---

## etj_snapHUDHLColor1
Name                    | values        | default
------------------------|:-------------:|-------------
etj_snapHUDHLColor1     | [any color](../index.md#color-system) | 1.0 0.5 1.0 0.75

Sets the primary highlight color of velocity snapping HUD.

---

## etj_snapHUDHLColor2
Name                    | values        | default
------------------------|:-------------:|-------------
etj_snapHUDHLColor2     | [any color](../index.md#color-system) | 1.0 0.5 1.0 0.1

Sets the secondary highlight color of velocity snapping HUD.

---

## etj_snapHUDOffsetY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_snapHUDHeight       | any integer   | 0

Changes Y-axis position of the velocity snapping HUD.

---

## etj_snapHUDTrueness
Name                    | values        | default
------------------------|:-------------:|-------------
etj_snapHUDTrueness     | bitflag       | 0

Set "trueness" flags on velocity snapping HUD.

* **1** Show upmove influence
* **2** Show true groundzones

---

## etj_spectatorInfoShadow
Name                    | values        | default
------------------------|:-------------:|-------------
etj_spectatorInfoShadow | 0 or 1        | 1

Toggles shadow on spectator list.

---

## etj_spectatorInfoSize
Name                    | values        | default
------------------------|:-------------:|-------------
etj_spectatorInfoSize   | any value     | 2.3

Sets the font size of spectator list.

---

## etj_spectatorInfoX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_spectatorInfoX      | any integer   | 320

Changes horizontal position of spectator list.

---

## etj_spectatorInfoY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_spectatorInfoY      | any integer   | 30

Changes vectical position of spectator list.

---

## etj_speedAlign
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedAlign          | 0 - 2         | 0

Set the alignment of ETJump speedometer.

* **0** Center
* **1** Left align
* **2** Right align

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
etj_speedColor          | [any color](../index.md#color-system) | White

Sets ETJump speedometer color.

_Note: use [`etj_speedAlpha`](etjump_cvars.md/#etj_speedalpha) to set alpha._

---

## etj_speedColorUsesAccel
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedColorUsesAccel | 0 - 2         | 0

Changes ETJump speedometer color to represent acceleration or deceleration.

* **1** simple, green if accelerating, red if decelerating, white if no input
* **2** advanced, takes into account per vector and current movement direction
    * green - optimal acceleration
    * yellow - suboptimal acceleration relative to movement direction
    * red - no acceleration towards movement direction
    * white - no input

_Note: due to inaccuracies in interpolation, advanced coloring is disabled while spectating and in demo playback, and simple acceleration coloring is used instead._

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

* **1** surfaces (always shown)
* **2** culling
* **3** viewcluster
* **4** dlights
* **5** render distance
* **6** flares
* **7** decals

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

* **0** for UPS 
* **1** for MPH
* **2** for KPH

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
etj_speedY              | any integer   | 320

Vertical position of the ETJump speedometer.

---

## etj_strafeQualityColor
Name                    | values        | default
------------------------|:-------------:|-------------
etj_strafeQualityColor  | [any color](../index.md#color-system) | 1.0 1.0 1.0 1.0

Set color of strafe quality display.

---

## etj_strafeQualityShadow
Name                    | values        | default
------------------------|:-------------:|-------------
etj_strafeQualityShadow | 0 or 1        | 1

Draw shadow on strafe quality display.

---

## etj_strafeQualitySize
Name                    | values        | default
------------------------|:-------------:|-------------
etj_strafeQualitySize   | any value     | 3

Set the size of strafe quality display.

---

## etj_strafeQualityStyle
Name                    | values        | default
------------------------|:-------------:|-------------
etj_strafeQualityStyle  | 0 - 2         | 0

Set the style of strafe quality display.

* **0** `Strafe quality: <value>%`
* **1** `<value>%`
* **2** `<value>`

---

## etj_strafeQualityX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_strafeQualityX      | any value     | 0

X offset of strafe quality display.

---

## etj_strafeQualityY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_strafeQualityY      | any value     | 0

Y offset of strafe quality display.

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

* **1** only picks up weapons dropped by you or spawned in map.
* **2** picks up all weapons.

_Note: this cvar has no effect unless `cg_autoactivate` is set to **1**._

---

## etj_uphillSteps
Name                    | values        | default
------------------------|:-------------:|-------------
etj_uphillSteps         | 0 or 1        | 1

Play footsteps on very low landing speeds.

---

## etj_upmoveMeterGraphColor
Name                      | values        | default
--------------------------|:-------------:|-------------
etj_upmoveMeterGraphColor | [any color](../index.md#color-system) | mdgrey

Set the color of upmove meter graph.

---

## etj_upmoveMeterGraphH
Name                    | values        | default
------------------------|:-------------:|-------------
etj_upmoveMeterGraphH   | any value     | 80

Set the height of upmove meter graph.

---

## etj_upmoveMeterGraphOnGroundColor
Name                              | values        | default
----------------------------------|:-------------:|-------------
etj_upmoveMeterGraphOnGroundColor | [any color](../index.md#color-system) | Green

Set the color of "on ground" bar on upmove meter graph.

---

## etj_upmoveMeterGraphOutlineColor
Name                              | values        | default
----------------------------------|:-------------:|-------------
etj_upmoveMeterGraphOutlineColor  | [any color](../index.md#color-system) | White

Set the color of upmove meter graph border.

---

## etj_upmoveMeterGraphOutlineW
Name                         | values        | default
-----------------------------|:-------------:|-------------
etj_upmoveMeterGraphOutlineW | any value     | 1

Set the width of upmove meter graph border.

---

## etj_upmoveMeterGraphPostJumpColor
Name                              | values        | default
----------------------------------|:-------------:|-------------
etj_upmoveMeterGraphPostJumpColor | [any color](../index.md#color-system) | Red

Set the color of "post jump" bar on upmove meter graph.

---

## etj_upmoveMeterGraphPreJumpColor
Name                              | values        | default
----------------------------------|:-------------:|-------------
etj_upmoveMeterGraphPreJumpColor  | [any color](../index.md#color-system) | Blue

Set the color of "pre jump" bar on upmove meter graph.

---

## etj_upmoveMeterGraphW
Name                    | values        | default
------------------------|:-------------:|-------------
etj_upmoveMeterGraphW   | any value     | 6

Set the width of upmove meter graph.

---

## etj_upmoveMeterGraphX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_upmoveMeterGraphX   | any value     | 8

Set the X position of upmove meter graph.

_Note: acts as a baseline position for text elements as well, even when graph isn't drawn._

---

## etj_upmoveMeterGraphY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_upmoveMeterGraphY   | any value     | 8

Set the Y position of upmove meter graph.

_Note: acts as a baseline position for text elements as well, even when graph isn't drawn._

---

## etj_upmoveMeterMaxDelay
Name                    | values        | default
------------------------|:-------------:|-------------
etj_upmoveMeterMaxDelay | any integer   | 360

Set the maximum tracked value in milliseconds for each upmove meter element to display.

---

## etj_upmoveMeterTextColor
Name                     | values        | default
-------------------------|:-------------:|-------------
etj_upmoveMeterTextColor | [any color](../index.md#color-system) | White

Set the color of "pre jump" bar on upmove meter graph.

---

## etj_upmoveMeterTextH
Name                    | values        | default
------------------------|:-------------:|-------------
etj_upmoveMeterTextH    | any value     | 12

Set the vertical spacing of upmove meter text elements.

---

## etj_upmoveMeterTextShadow
Name                      | values        | default
--------------------------|:-------------:|-------------
etj_upmoveMeterTextShadow | 0 or 1        | 1

Draw shadow on upmove meter text.

---

## etj_upmoveMeterTextSize
Name                      | values        | default
--------------------------|:-------------:|-------------
etj_upmoveMeterTextSize   | any value     | 2

Set the size of upmove meter text elements.

---

## etj_upmoveMeterTextX
Name                      | values        | default
--------------------------|:-------------:|-------------
etj_upmoveMeterTextX      | any value     | 6

Set the horizontal distance of upmove meter text elements relative to the graph.

---

## etj_viewlog
Name                    | values        | default
------------------------|:-------------:|-------------
etj_viewlog             | 0 or 1        | 1

Toggles an external console window, mainly used for copy pasting etc. Unlocked version of `viewlog`.

_Note: ET: Legacy client requires you to start the game with `+set viewlog 1`, the console window cannot be created while the game is running._

---

## etj_viewPlayerPortals
Name                    | values        | default
------------------------|:-------------:|-------------
etj_viewPlayerPortals   | 0 - 2         | 1

Toggles other players portals. 

* **0** don't show
* **1** always show
* **2** show when spectating

---

## etj_weaponVolume
Name                    | values        | default
------------------------|:-------------:|-------------
etj_weaponVolume        | 0.0 - 1.0     | 1

Set the volume of weapon-related sounds.

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

Set draw distance. Setting this to **0** uses maps `farplanedist` value. Unlocked version of `r_zfar`.

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

_Note: values outside of **90-160** require `developer 1`._

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

_Note: values outside of **90-160** require `developer 1`._

---

## movie_fovMinSpeed
Name                    | values        | default
------------------------|:-------------:|-------------
movie_fovMinSpeed       | any integer   | 400

UPS value at which minimum FOV is reached.

---
