# ETMain cvars

The following ETMain cvars have been modified or extended by ETJump.

---

## cg_autoswitch
Name                    | values        | default
------------------------|:-------------:|-------------
cg_autoswitch           | bitflag       | 0

Controls the behavior of automatic weapon switching.

* **0** disable autoswitching
* **1** enable autoswitch (required for other options)
* **2** don't autoswitch unless replacing currently held weapon
* **4** disable autoswitching to portalgun

```{hint}
ETJump has added additional control to the behavior of this cvar.
```

---

## cg_centertime
Name                    | values        | default
------------------------|:-------------:|-------------
cg_centertime           | any value     | 5

Defines how long center prints stay on screen. 

```{hint}
ETJump has removed cheat protection from this cvar.
```

---

## cg_crosshairSize
Name                    | values        | default
------------------------|:-------------:|-------------
cg_crosshairSize        | any value     | 48

Sets size of the crosshair.

```{hint}
ETJump allows using floating point values for this cvar.
```

---

## cg_crosshairX
Name                    | values        | default
------------------------|:-------------:|-------------
cg_crosshairX           | any value     | 0

Sets horizontal offset for the crosshair. 

```{hint}
ETJump allows using floating point values for this cvar.
```

---

## cg_crosshairY
Name                    | values        | default
------------------------|:-------------:|-------------
cg_crosshairY           | any value     | 0

Sets vertical offset for the crosshair.

```{hint}
ETJump allows using floating point values for this cvar.
```

---

## cg_drawCrosshair
Name                    | values        | default
------------------------|:-------------:|-------------
cg_drawCrosshair        | 0 - 16        | 1

Sets the crosshair variant to draw.

* **0-9** default crosshairs
* **10** vertical line
* **11** cross
* **12** diagonal cross
* **13** V-shape
* **14** triangle
* **15** T-shape
* **16** two vertical lines

```{hint}
ETJump has added crosshairs **10-16**.
```

---

## cg_drawWeaponIconFlash
Name                    | values        | default
------------------------|:-------------:|-------------
cg_drawWeaponIconFlash  | 0 - 2         | 0

Draws weapon icon with different colors depending on state of weapon.

* **1**
    * yellow = ready/reloading
    * red = shooting
    * white = switching
* **2**
    * white - ready
    * yellow - reloading/switching
    * red - shooting

```{hint}
ETJump has added value **2**, which mimics ETPro/legacy behavior for the weapon icon flash.
```

---

## cg_gunX/Y/Z
Name                    | values        | default
------------------------|:-------------:|-------------
cg_gunX/Y/Z             | any value     | 0

Moves gun viewmodel on X/Y/Z axes, respectively. 

```{hint}
ETJump has removed cheat protection from these cvars.
```

---

## cg_lagometer
Name                    | values        | default
------------------------|:-------------:|-------------
cg_lagometer            | 0 - 2         | 0

Draws lagometer, showing connection quality to server.

* **1** Draw lagometer on online servers and demo playback
* **2** Draw lagometer also on localhost

```{hint}
ETJump has added value **2**.
```

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

```{hint}
ETJump has changed this cvar to a bitflag, and added values **2**, **8** and **16**.
```

---

## cg_skybox
Name                    | values        | default
------------------------|:-------------:|-------------
cg_skybox               | 0 or 1        | 1

Toggles drawing of skyportal skyboxes.

```{hint}
ETJump has removed cheat protection from this cvar.
```

---

## cg_teamChatHeight
Name                    | values        | default
------------------------|:-------------:|-------------
cg_teamChatHeight       | 0 - 64        | 8

Sets the maximum number of chat lines to draw on screen.

```{note}
Despite the name, this affects all types of chat messages.
```

```{hint}
ETJump has increased the maximum from **8** to **64**.
```

---
