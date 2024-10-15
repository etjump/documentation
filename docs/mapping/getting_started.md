# Mapping for ETJump

Here you will find simple guide on how to start mapping for ETJump mod.

```{admonition} Under construction
:class: seealso

The contents of this pages are in need of a refresh, and will be updated in the future
```

---

## Getting started

To start mapping it's **HIGHLY RECOMMENDED** to make a clean ET install seperate from your regular ET install. This way you won't accidentally use custom assets provided by other maps in your map. A third, untouched install could also come in handy when creating a pk3. This install should only be used to test if you have included every custom asset in your pk3.

---

## Tools

To create maps, you need an id Tech 3 compatible level editor. Two of the most commonly used ones are **NetRadiant** (specifically netradiant-custom by Garux) and **GtkRadiant**.

- [Download NetRadiant-custom](https://github.com/Garux/netradiant-custom)
- [Download GtkRadiant](http://icculus.org/gtkradiant/)

NetRadiant-custom is the recommended editor for mapping. It includes much more advanced tooling compared to GtkRadiant, such as full editing capabilities in 3D window, UV tool and much improved CSG tool. It also provides hardware accelerated 3D window, fully customizeable keyboard shortcuts, WASD camera controls, customizeable build menu, new mouse shortcuts, XML-formatted entity definition with support for default values, dropdowns and checkboxes in entity inspector, and much more.

In order to play your own maps you create, you will need the ETJump server module. This is not included in PK3 file that you download from a server, so grab the full zip file for the mod from [ETJump website](https://etjump.com/).

```{hint}
Server modules for all supported platforms are included in the zip file. The platform specific files are:

* `qagame_mp_x86/64.dll` on Windows x86/64, respectively
* `qagame.mp.i386/x86_64.so` on Linux x86/64, respectively
* `qagame_mac` on macOS, for both Intel x64 and ARM64 (universal binary).
```

It's also recommended to download a more advanced text editor for editing shaders and script files. Below are some options.

- [Notepad++](https://notepad-plus-plus.org/)
- [Sublime Text](https://www.sublimetext.com/)
- [Visual Studio Code](https://code.visualstudio.com/)

Both [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=mjxcode.vscode-q3shader) and [Sublime Text](https://github.com/isRyven/Sublime-Text-Q3Script) have plugins for idTech 3 syntax highlighting.

[Pack3r](https://github.com/ovska/Pack3r) is a tool for automatically generating release-ready PK3 files for ET maps. See the repository readme for usage instructions.

---

## ETJump mapping assets

ETJump assets include entities and shaders that are useful when creating maps for ETJump.
You can get the assets from [ETJump mapping repository](https://github.com/etjump/mapping).

---

## ETJump mapping entities

While creating your map, you most likely want to use entities provided by ETJump. Along with explanations provided in entity file, you can check the documentation on how to use ETJump specific entities. See the full list {doc}`here <mapping_entities>`.
