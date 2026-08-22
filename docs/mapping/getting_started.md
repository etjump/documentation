# Mapping for ETJump

Here you will find simple guide on how to start mapping for ETJump mod.

---

## TL;DR

Already familiar with the setup, but just need a refresher of the order of the steps?

* Create clean mapping installation
* Install [NetRadiant-custom](https://github.com/Garux/netradiant-custom/releases)
* Install [ET Mapping SDK](https://aciz.etjump.com/downloads/et-mapping-sdk.zip)
* Install [ETJump mapping assets](https://github.com/etjump/mapping)
* (Optional) Install [ET extra assets](https://github.com/Aciz/ET-extra-assets)

---

## Getting started

This section explains the steps to follow in order to setup a proper mapping environment.

---

### Create a mapping installation

To start mapping it's **HIGHLY RECOMMENDED** to make a clean ET install seperate from your regular ET install. This way you won't accidentally use custom assets provided by other maps in your map, and every custom asset you use is a deliberate choice, thus the assets required by the map stay clearer. A third, untouched install could also come in handy when creating a pk3. This install should only be used to test if you have included every custom asset in your pk3.

You can use an installer to create a separate installation, or simply copy the files manually. If you choose to copy over the files, the directory structure you end up should be the following:

```
├── <engine of your choosing>
├── etmain/
│   ├── pak0.pk3
│   ├── pak1.pk3
│   └── pak2.pk3
└── etjump/
    ├── etjump-X.Y.Z.pk3
    ├── qagame.mp.i386.so (Linux 32-bit)
    ├── qagame.mp.x86_64.so (Linux 64-bit)
    ├── qagame_mac (macOS 64-bit)
    ├── qagame_mp_x64.dll (Windows 64-bit)
    └── qagame_mp_x86.dll (Windows 32-bit)
```

```{note}
* To get the ETJump server modules (`qagame*` files), download the full release zip from the [ETJump website](https://etjump.com/). You only need to one that matches your platform and client architecture, but having all of them installed does not hurt.
* You may optionally also copy over `mp_bin.pk3` into `etmain` directory - this contains `etmain` cgame/ui binaries, if you ever want to run `etmain` as the mod, instead of ETJump. Note that `etmain` only runs on 32-bit Windows and Linux.
* If you're using ET: Legacy on Linux, make sure you also copy over the renderer library:
  * `librenderer_opengl1_i386.so` (32-bit client)
  * `librenderer_opengl1_x86_64.so` (64-bit client)
```

---

### Install NetRadiant-custom

To create maps, you need an id Tech 3 compatible level editor. The recommended editor for this is [**NetRadiant-custom**](https://github.com/Garux/netradiant-custom/releases). There is no installer available, you simply extract the archive. Avoid using write protected directories, such as `Program Files`, as the editor needs to write some files to the installation directory on first setup.

At this point, you may run Radiant once to see if everything works, and point it to the mapping installation we created earlier. Note that you should point it to the **root of the installation (where the game executable is), not `etmain` directory!** If you see the stock game assets, you can continue to the next step. If no textures/shaders are visible, double check the paths you setup by going to `Edit -> Preferences -> Paths`. The `Engine Path` should point to the directory where your game executable is - a common mistake is to point this to `etmain` directory.

---

### Install ET mapping SDK

NetRadiant-custom, unlike GtkRadiant, does not install the ET mapping SDK for you. You must manually install this, otherwise your installation will lack editor images for common shaders, as well as most stock ET models for example.

Download the SDK [here](https://aciz.etjump.com/downloads/et-mapping-sdk.zip). Extract it to your mapping installation you created earlier, overwriting anything if prompted. Once extracted, the directory structure should be like this:

```
├── etmain/
├── etmain/
│   ├── pak0.pk3
│   ├── pak1.pk3
│   ├── pak2.pk3
│   ├── astro-skies.pk3
│   ├── common.pk3
│   ├── goldrush.pcx
│   ├── lights.pk3
│   ├── scripts/
│   │   ├── shaderlist.txt
│   │   ├── default_project.proj
│   │   ├── default_shaderlist.txt
│   │   ├── et_entities.def
│   │   └── <bunch of .shader files>
│   ├── maps/
│   │   └── goldrush.map
│   └── models/
│       └── mapobjects/
│           └── <lots of directories with models>
└── etjump/
    ├── etjump-X.Y.Z.pk3
    ├── qagame.mp.i386.so
    ├── qagame.mp.x86_64.so
    ├── qagame_mac
    ├── qagame_mp_x64.dll
    └── qagame_mp_x86.dll

```

---

### Install ETJump mapping assets

To create ETJump maps, you will also want to install the ETJump mapping assets. This includes ETJump entities, and common shaders used to create thing such as `nosave` areas. Head on over to the [ETJump mapping repository](https://github.com/etjump/mapping) to get the necessary files. The repository readme contains the installation instructions, but here are the steps outlined.

* Download the repository as a zip file and extract it to your mapping installation directory, overwriting any files as prompted (or use Git to clone it, if you prefer).
* Navigate to the `scripts` directory and locate `et_entities.ent` (**NOTE:** not `et_entities.def`) and copy this over to your `<radiant install directory>/gamepacks/et.game/etmain/` directory, overwriting the existing file.
* Navigate back to the `scripts` directory, and open `shaderlist.txt` with a text editor of your choosing, and add `lightblock` at the bottom of the file, on a separate line.

Now start up Radiant and see that the assets are installed correctly. You should see ETJump entities as you right-click on a 2D view, and `common` shaders should have all the ETJump common shaders. If everything is working, you are now ready to start mapping!

---

### (Optional) Get ET Extra assets

The stock ET installation + SDK setup is not fully complete - it's missing some assets used in the original maps. You may grab these missing assets [here](https://github.com/Aciz/ET-extra-assets). Please see the readme in the repository for instructions and further information on what is included.

---

### (Optional) Setup pk3dir directories

```{caution}
`.pk3dir` directories are not supported by ET 2.60b.
```

You may have already extracted `pak0.pk3` inside your mapping directory even if it wasn't explicitly instructed. If you haven't - good. Consider using a `pak0.pk3dir` instead.

`.pk3dir` directories are special directories that mirror the structure of a pk3 file. These are fully transparent to the game and Radiant - they are read just as any packaged pk3 file. Using these is **highly recommended** to help keeping your mapping installation organized. You should always create a `.pk3dir` directory for each project you work on, instead of dumping all assets to the common directories inside `etmain`.

As you'll likely want to extract `pak0.pk3` (not strictly necessary, but useful for browsing the files), create a `pak0.pk3dir` directory inside `etmain` directory of your mapping installation. Extract `pak0.pk3` inside this directory. You should end up with a directory structure like this:

```
└── etmain/
    └── pak0.pk3dir/
        ├── animations/
        ├── botfiles/
        ├── characters/
        ├── fonts/
        ├── gfx/
        ├── icons/
        ├── levelshots/
        ├── maps/
        ├── menu/
        ├── models/
        ├── scripts/
        ├── sound/
        ├── sprites/
        ├── text/
        ├── textures/
        ├── ui/
        ├── weapons/
        └── <rest of the files>
```

As you can see, we have all the usual directories here - `maps`, `textures`, `scripts`, `models` etc. This helps keep track of what assets belong to which project. You can imagine this being a directory for your current project - `etmain/mymap.pk3dir` contains every custom asset you use for your project. Once you are finished, it's easy to remove all the custom assets that the project uses too, if you prefer to keep your Radiant installation clean of any unnecessary custom assets.

---

## Tools

Below is a list of useful tools to aid you with mapping.

---

### Text editors
* [Notepad++](https://notepad-plus-plus.org/)
* [Sublime Text](https://www.sublimetext.com/)
* [Visual Studio Code](https://code.visualstudio.com/)

Both [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=mjxcode.vscode-q3shader) and [Sublime Text](https://github.com/isRyven/Sublime-Text-Q3Script) have plugins for idTech 3 syntax highlighting.

---

### PK3 creation
* [Pack3r](https://github.com/ovska/Pack3r) - scans your `.map` file and creates a release-ready pk3 file, including all custom assets. CLI only.
* [QtPack3r](https://github.com/Aciz/QtPack3r/) - graphical front-end for Pack3r.

---

### Misc
* [Overbounce calculator](https://etjump.com/utilities/overbounce/)
* [Overbounce list](https://q3df.org/wiki?p=189)
* [Blender BSP/MAP/MD3 import/export plugin](https://github.com/SomaZ/Blender_BSP_Importer/releases)

---

## Further reading

To get familiar with ETJump-specific [entities](mapping_entities.md) and [mapscripting](mapscripting.md), check out the corresponding pages.
