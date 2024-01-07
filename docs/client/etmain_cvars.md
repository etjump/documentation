# ETMain cvars

The following ETMain cvars have been modified or extended by ETJump.

---

## cg_drawCrosshair
Name                    | values        | default
------------------------|:-------------:|-------------
cg_drawCrosshair        | 0 - 16        | 1

ETJump includes additional crosshairs.

* **10** Vertical line
* **11** Cross
* **12** Diagonal cross
* **13** V-shape
* **14** Triangle
* **15** T-shape
* **16** Two vertical lines

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

## cg_drawWeaponIconFlash
Name                    | values        | default
------------------------|:-------------:|-------------
cg_drawWeaponIconFlash  | 0 - 2         | 0

Draws weapon icon with different colors depending on state of weapon.

* cg_drawWeaponIconFlash 1
    * yellow = ready/reloading
    * red = shooting
    * white = switching
* cg_drawWeaponIconFlash 2
    * white - ready
    * yellow - reloading/switching
    * red - shooting

_ETJump has added value 2._

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

* **1** Draw lagometer on online servers and demo playback
* **2** Draw lagometer also on localhost

---

## cg_showmiss
Name                    | values        | default
------------------------|:-------------:|-------------
cg_showmiss             | bitflags      | 0

Outputs prediction related events and errors to console.

* **1** General prediction information
* **2** Output statistics of predicted/played back frames
* **4** Output client pmove timestamps and cgame time timestamps
* **8** Output prediction error codes
* **16** Output info if player didn't move this frame

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
