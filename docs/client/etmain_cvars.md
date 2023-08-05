# ETMain cvars

The following ETMain cvars have been modified or extended by ETJump.

---

## cg_drawCrosshair
Name                    | values        | default
------------------------|:-------------:|-------------
cg_drawCrosshair        | 0 - 16        | 1

ETJump includes additional crosshairs.

* __10__ Vertical line
* __11__ Cross
* __12__ Diagonal cross
* __13__ V-shape
* __14__ Triangle
* __15__ T-shape
* __16__ Two vertical lines

---

## cg_centertime
Name                    | values        | default
------------------------|:-------------:|-------------
cg_centertime           | any value     | 5

Defines how long center prints stay on screen. 

_ETJump has removed `CVAR_CHEAT` flag from this cvar._

---

## cg_crosshairSize
Name                    | values        | default
------------------------|:-------------:|-------------
cg_crosshairSize        | any value     | 48

Sets the size of crosshair.

_ETJump allows using floating point values for this cvar._

---

## cg_crosshairX
Name                    | values        | default
------------------------|:-------------:|-------------
cg_crosshairSize        | any value     | 0

Offsets crosshairs horizontal position. 

_ETJump allows using floating point values for this cvar._

---

## cg_crosshairY
Name                    | values        | default
------------------------|:-------------:|-------------
cg_crosshairSize        | any value     | 0

Offsets crosshairs vertical position

_ETJump allows using floating point values for this cvar._

---

## cg_gunX/Y/Z
Name                    | values        | default
------------------------|:-------------:|-------------
cg_gunX/Y/Z             | any value     | 0

Moves gun viewmodel on X/Y/Z axes, respectively. 

_ETJump has removed `CVAR_CHEAT` flag from these cvars._

---

## cg_lagometer
Name                    | values        | default
------------------------|:-------------:|-------------
cg_lagometer            | 0 - 2         | 0

Draws lagometer, showing connection quality to server.

* __1__ Draw lagometer on online servers and demo playback
* __2__ Draw lagometer also on localhost

---

## cg_showmiss
Name                    | values        | default
------------------------|:-------------:|-------------
cg_showmiss             | bitflags      | 0

Outputs prediction related events and errors to console.

* __1__ General prediction information
* __2__ Output statistics of predicted/played back frames
* __4__ Output client pmove timestamps and cgame time timestamps
* __8__ Output prediction error codes
* __16__ Output info if player didn't move this frame

---

## cg_skybox
Name                    | values        | default
------------------------|:-------------:|-------------
cg_skybox               | 0 or 1        | 1

Toggles drawing of skyportal skyboxes.

_ETJump has removed `CVAR_CHEAT` flag from this cvar._

---

## cg_teamChatHeight
Name                    | values        | default
------------------------|:-------------:|-------------
cg_teamChatHeight       | 0 - 64        | 8

Sets the maximum number of chat lines to draw on screen.

_ETJump has increased the maximum from ***8*** to ***64***._

---
