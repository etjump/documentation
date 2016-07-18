# List of ETJump client cvars
Below is a list of all ETJump related cvars (console variables) for players.

---

## etj_altScoreboard
Name                    | values        | default
------------------------|:-------------:|-------------
etj_altScoreboard       | 0 - 2         | 2

Changes the scoreboard to an alternative one. 0 for default scoreboard, 1 for alternative scoreboard 1, 2 for alternative scoreboard 2.

---

## etj_CGazAlpha
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGazAlpha           | 0.0 - 1.0     | 0.15

How transparent CGaz meter is.

---

## etj_CGazHeight
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGazHeight          | Any integer   | 20

Height of the CGaz meter.

---

## etj_CGazWidth
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGazWidth           | Any integer   | 300

Width of the CGaz meter.

---

## etj_CGazY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_CGazY               | Any integer   | 260

Vertical position of CGaz meter.

---

## etj_chatBackgroundAlpha
Name                    | values        | default
------------------------|:-------------:|-------------
etj_chatBackgroundAlpha | 0.0 - 1.0     | 0.33

How transparent chat box is.

---

## etj_chatFlags
Name                    | values        | default
------------------------|:-------------:|-------------
etj_chatFlags           | 0 or 1        | 1

Toggles drawing chat flags.

---

## etj_chatPosX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_chatPosX            | any integer   | 0

Chat box horizontal location.

---

## etj_chatPosY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_chatPosY            | any integer   | 0

Chat box vertical location.

---

## etj_CHS1Info__X__
Where __X__ stands for integer of __1__ to __8__ specifing text position on the circle.
See full list of parameters [here](/index.md#chs).

---

## etj_CHS2Info__X__
Where __X__ stands for integer of __1__ to __8__ specifing text position in the list.
See full list of parameters [here](/index.md#chs).

---

## etj_drawCGaz
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawCGaz            | 0 - 4         | 0

Draws the CGaz meter.

---

## etj_drawCGazUsers
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawCGazUsers       | 0 or 1        | 1

Shows whether users are using CGaz in the original scoreboard.

---

## etj_drawCHS1
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawCHS1            | 0 or 1        | 0

Draws crosshair stats 1.

---

## etj_drawCHS2
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawCHS2            | 0 or 1        | 0

Draws crosshair stats 2.

---

## etj_drawClock
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawClock           | 0 - 2        | 1

Draws clock. 1 for 24-hour clock, 2 for 12-hour clock.

---

## etj_drawConnectionIssues
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawConnectionIssues | 0 or 1       | 1

Toggles drawing of connection interrupted text if there are connection problems.

---

## etj_drawKeys
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawKeys            | 0 or 1        | 1

Draws pressed keys.

---

## etj_drawMessageTime
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawMessageTime     | 0 - 2         | 2

Draw when a message was sent. 1 for hours:minutes format, 2 for hours:minutes:seconds format.

---

## etj_drawOB
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawOB              | 0 or 1        | 0

Draws overbounce meter. 1 for simple overbounce meter, 2 for advanced.

---

## etj_drawRunTimer
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawRunTimer        | 0 or 1        | 1

Draws the timerun timer.

---

## etj_drawSlick
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawSlick           | 0 or 1        | 1

Draws slick detector.

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

Draws original ETPub-style speedometer. 2 to also draw max speed. Reset with `resetmaxspeed`.

---

## etj_drawSpeed2
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawSpeed2          | 0 or 1        | 1

Draws ETJump speedometer.

---

## etj_drawTokens
Name                    | values        | default
------------------------|:-------------:|-------------
etj_drawTokens          | 0 or 1        | 1

Toggles drawing of collectible tokens in original maps.

---

## etj_enableTimeruns
Name                    | values        | default
------------------------|:-------------:|-------------
etj_enableTimeruns      | 0 or 1        | 1

Toggles timeruns.

---

## etj_explosivesShake
Name                    | values        | default
------------------------|:-------------:|-------------
etj_explosivesShake     | 0 - 3         | 3

Controls screenshake from explosives. 0 to disable screenshakes, 1 to disable for own explosives, 2 to disable for other player's explosives, 3 for default behaviour.

---

## etj_ghostPlayersAlt
Name                    | values        | default
------------------------|:-------------:|-------------
etj_ghostPlayersAlt     | 0 or 1        | 0

Toggles alternative drawing of other players. When enabled, a single shader is used to draw other players. [Example](http://i.imgur.com/yJaQ1be.png).

---

## etj_ghostPlayersColor
Name                    | values        | default
------------------------|:-------------:|-------------
etj_ghostPlayersColor   | 0.0 - 1.0     | "1.0 1.0 1.0"

Changes player color when `etj_ghostPlayersAlt` is enabled.

---

## etj_ghostPlayersFadeRange
Name                    | values        | default
------------------------|:-------------:|-------------
etj_ghostPlayersFadeRange | Any integer | 200

Additional range added to `etj_hideDistance` where other players start to fade before disappearing completely.

---

## etj_ghostPlayersOpacity
Name                    | values        | default
------------------------|:-------------:|-------------
etj_ghostPlayersOpacity | 0.0 - 1.0     | 1.0

Opacity of other players when `etj_ghostPlayersAlt` is enabled.

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
etj_hideDistance        | Any integer   | 128

How close a player has to be to be hidden from view.

---

## etj_hideMe
Name                    | values        | default
------------------------|:-------------:|-------------
etj_hideMe              | 0 or 1        | 0

Hides yourself.

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
etj_keysColor           | red, cyan, white, etc | White

Set the color of pressed keys view.

---

## etj_keysSize
Name                    | values        | default
------------------------|:-------------:|-------------
etj_keysSize            | Any integer   | 48

Set the size of pressed keys view.

---

## etj_keysX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_keysX               | any integer   | 585

Set the horizontal position of pressed keys view.

---

## etj_keysY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_keysY               | any integer   | 200

Set the vertical position of pressed keys view.

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

Prints banner text into console.

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
etj_noclipScale         | 1 - 20        | 1

Scales the noclip speed.

---

## etj_nofatigue
Name                    | values        | default
------------------------|:-------------:|-------------
etj_nofatigue           | 0 or 1        | 1

Toggle nofatigue.

---

## etj_numPopups
Name                    | values        | default
------------------------|:-------------:|-------------
etj_numPopups           | 0 - 32        | 5

Maximum amount of popups to display.

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
etj_popupGrouped        | 0 or 1        | 1

Groups identical repetitive popup messages into one. 

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

## etj_runTimerShadow
Name                    | values        | default
------------------------|:-------------:|-------------
etj_runTimerShadow      | 0 or 1        | 0

Draws shadow under run timer.

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

How transparent speedometer 2 is.

---

## etj_speedColor
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedColor          | red, cyan, white, etc | White

Color of the speedometer 2.

---

## etj_speedinterval
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedinterval       | any integer   | 100

How often speedometer 1 gets updated in milliseconds.

---

## etj_speedShadow
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedShadow         | 0 or 1        | 0

Draws shadow under speedometer 2.

---

## etj_speedSizeX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedSizeX          | any integer   | 3

Horizontal size of speedometer 2.

---

## etj_speedSizeY
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedSizeY          | any integer   | 3

Vertical size of speedometer 2.

---

## etj_speedunit
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedunit           | 0 - 2         | 0

Speedometer 1 units. 0 for UPS, 1 for MPH, 2 for KPH.

---

## etj_speedX
Name                    | values        | default
------------------------|:-------------:|-------------
etj_speedX              | any integer   | 320

Horizontal position of the speedometer 2.

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

Vertical position of the speedometer 2.

---

## etj_stretchCgaz
Name                    | values        | default
------------------------|:-------------:|-------------
etj_stretchCgaz         | 0 or 1        | 1

Stretches CGaz when using widescreen aspect ratio.

---

## etj_viewlog
Name                    | values        | default
------------------------|:-------------:|-------------
etj_viewlog             | 0 or 1        | 1

Show an external console log for copy pasting etc.

---

## etj_viewPlayerPortals
Name                    | values        | default
------------------------|:-------------:|-------------
etj_viewPlayerPortals   | 0 or 1        | 1

Show other players portals. 0 don't show, 1 always show, 2 show when spectating.

---

## etj_weaponSound
Name                    | values        | default
------------------------|:-------------:|-------------
etj_weaponSound         | 0 or 1        | 1

Play weapon sound when firing a weapon.

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
movie_fovMax            | 90 - 140      | 140

Maximum value FOV can increase to.

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
movie_fovMin            | 90 - 140      | 90

Starting value of speed-based fov.

---

## movie_fovMinSpeed
Name                    | values        | default
------------------------|:-------------:|-------------
movie_fovMinSpeed       | any integer   | 400

UPS value at which FOV starts to increase.

---
