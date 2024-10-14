# Getting started with ETJump
This page contains useful information about the general features of the mod. It's a good starting point for newcomers to get familiar with the mod.

```{admonition} Under construction
:class: seealso

This page is a work in progress. The old "Getting Started" page was split into three separate pages without much of new content. This will be filled with more information in the future.
```

---

## Things everyone should know

### Framerate independent physics
You should always have `pmove_fixed` set to **1**. This is the de-facto standard for physics calculations in ETJump. This forces the game to calculate physics at exactly **8ms** intervals, regardless of you actual framerate, ensuring consistent behavior for acceleration and jump height.

```{caution}
Do not use `pmove_fixed 1` while playing other mods! It negatively affects several aspects of regular gameplay, such as bullet spread.
```

---

### Unlimited stamina
ETJump gives players access to permanent adrenaline with [`etj_nofatigue`](client/etjump_cvars.md/#etj_nofatigue) cvar, giving you unlimited stamina. This means it's not required to reapply adrenaline constantly in order to not lose stamina.

---

### Client framerate
Because of `pmove_fixed 1`, your actual client framerate does not matter. It can be set to any number (though preferrably **125** or higher) without affecting gameplay.

```{note}
A common historical misconception is that you should lock your FPS to either **43**, **76** or **125**, depening on which framerate is stable on your system. This is only true when you use `pmove_fixed 0`, which you should never have while playing ETJump.
```

```{note}
Setting `com_maxFPS` to **333** and disabling `pmove_fixed` gives you additional jump height. This is generally considered cheating, and might [not be allowed](server/server_cvars.md/#g_blockcheatcvars) on a server.
```

---

### Field of View
Often times your movements speed is in hundreds or thousands of units per second. Because of this, most players like to raise their `cg_fov` value from the default, for visual clarity and to reduce motion sickness. ETJump also allows you to [`change the way FOV is calculated`](client/etjump_cvars.md/#etj_realfov) in order to better support modern widescreen resolutions.

---

## Color system
ETJump includes an improved color parsing system for cvars that expect color values. The following formats are supported:

Format                       | Example value
:----------------------------|:------------------------
string                       | white, black, green etc.
normalized `<r> <g> <b> [a]` | 1.0 0.5 0.75 0.33
full `<r> <g> <b> [a]`       |  255 128 191
hex color                    |  #ff80bf, 0xff80bf

There is no need to indicate in any way which type of color you're using - the mod will detect this automatically.

```{note}
An RGB(A) value is considered full RGB(A) if one of the color components (R, G or B) is over **1**. Alpha defaults to **1.0** if it's excluded from a value.
``` 

This color system will work with any mod-sided cvar (generally anything that starts with `etj_` or `cg_`) that takes in a color as a value.

```{note}
Some elements have a separate "color" and "alpha" cvars. In these cases, the alpha component is ignored on the "color" cvar parsing. Such cases are documented in the [cvar documentation](client/etjump_cvars.md).
```
