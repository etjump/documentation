# Basic features

This page contains an introduction to the basic features of ETJump.

```{admonition} Under construction
:class: seealso

This page is a work in progress. The old "Getting Started" page was split into three separate pages without much of new content. This will be filled with more information in the future.
```

---

## Position saving and loading
ETJump offers players to ability to [`save`](client/client_commands.md/#save) and [`load`](client/client_commands.md/#load) their position. It's recommended to bind these keys to conveniently available buttons, such as `mouse4/5` or `q/e` for easy access, as you will be needing them often.

By default when you load a saved position, your viewangles are restored to match the angles you had when saving. Some players find this distracting, and it can be turned off by setting the [`etj_loadviewangles`](client/etjump_cvars.md/#etj_loadviewangles) cvar to **0**.

```{tip}
Saves are unique per team. A saved position created while playing on Allies cannot be loaded while playing on Axis.
```

```{tip}
There are 3 different saveslots available for each team, which can be accessed by typing `save/load 0/1/2`. By default, slot **0** is used.
```

```{seealso}
* [`backup`](client/client_commands.md/#backup)
* [`unload`](client/client_commands.md/#unload)
```

---

## Speed meter
ETJump offers you two different speed meters to see how fast you're going. These are both visible by default.

[`etj_drawspeed`](client/etjump_cvars.md/#etj_drawspeed)  
![etj_drawspeed](img/etj_drawspeed.gif)

[`etj_drawSpeed2`](client/etjump_cvars.md/#etj_drawspeed2)  
![etj_drawSpeed2](img/etj_drawSpeed2.gif)

Both of the speed meters have several customization options.

```{admonition} etj_drawspeed
:class: seealso

* [`etj_speedinterval`](client/etjump_cvars.md/#etj_speedinterval)
* [`etj_speedunit`](client/etjump_cvars.md/#etj_speedunit)
* [`etj_speedXYOnly`](client/etjump_cvars.md/#etj_speedxyonly)
```

```{admonition} etj_drawSpeed2
:class: seealso

* [`etj_speedAlign`](client/etjump_cvars.md/#etj_speedalign)
* [`etj_speedAlpha`](client/etjump_cvars.md/#etj_speedalpha)
* [`etj_speedColor`](client/etjump_cvars.md/#etj_speedcolor)
* [`etj_speedColorUsesAccel`](client/etjump_cvars.md/#etj_speedcolorusesaccel)
* [`etj_speedShadow`](client/etjump_cvars.md/#etj_speedshadow)
* [`etj_speedSize`](client/etjump_cvars.md/#etj_speedsize)
* [`etj_speedX`](client/etjump_cvars.md/#etj_speedx), [`etj_speedY`](client/etjump_cvars.md/#etj_speedy)
```

```{tip}
It's also possible to display your momentary max speed. Refer to [`etj_drawMaxSpeed`](client/etjump_cvars.md/#etj_drawmaxspeed).
```

---

## Hiding & drawing other players
Collision with other players is disabled in ETJump by default. Because of this, it's often desired to hide other players, to prevent them from blocking your view. This is enabled by default, and can be toggled with the [`etj_hide`](client/etjump_cvars.md/#etj_hide) cvar.

```{tip}
If you don't want other players to see you even when player hiding is disabled, you can enable the [`etj_hideMe`](client/etjump_cvars.md/#etj_hideme) cvar.
```

It's also possible to draw other players using a simple, single colored shader by enabling the [`etj_drawSimplePlayers`](client/etjump_cvars.md/#etj_drawsimpleplayers) cvar.

![simple players example](img/simple_players_example.png)

```{seealso}
* [`etj_hideDistance`](client/etjump_cvars.md/#etj_hidedistance)
* [`etj_hideFadeRange`](client/etjump_cvars.md/#etj_hidefaderange)
* [`etj_playerOpacity`](client/etjump_cvars.md/#etj_playeropacity)
* [`etj_simplePlayersColor`](client/etjump_cvars.md/#etj_simpleplayerscolor)
```

---

## Pressed keys view
You can see what movement keys you are pressing by enabling [`etj_drawKeys`](client/etjump_cvars.md/#etj_drawkeys). This also works while spectating other players, which is a great way for new players to learn some of the more advanced techniques from more experienced players. You can choose one from the following keysets.

Keyset                                              | Value
:---------------------------------------------------|:---------------
![`etj_drawKeys 1`](img/etj_drawKeys1.jpg){w=80px} | `etj_drawKeys 1`
![`etj_drawKeys 2`](img/etj_drawKeys2.jpg){w=80px} | `etj_drawKeys 2`
![`etj_drawKeys 3`](img/etj_drawKeys3.jpg){w=80px} | `etj_drawKeys 3`
![`etj_drawKeys 4`](img/etj_drawKeys4.jpg){w=80px} | `etj_drawKeys 4`
![`etj_drawKeys 5`](img/etj_drawKeys5.jpg){w=80px} | `etj_drawKeys 5`


```{seealso}
* [`etj_keysColor`](client/etjump_cvars.md/#etj_keyscolor)
* [`etj_keysShadow`](client/etjump_cvars.md/#etj_keysshadow)
* [`etj_keysSize`](client/etjump_cvars.md/#etj_keyssize)
* [`etj_keysX`](client/etjump_cvars.md/#etj_keysx), [`etj_keysY`](client/etjump_cvars.md/#etj_keysy)
```

---

## Teleporting (to) other players
You can teleport to a location of another player on the server by using the [`goto`](client/client_commands.md/#goto) command. Similarly, you can teleport other players to your location using the [`call`](client/client_commands.md/#call-iwant) command.

```{note}
By default, you are not allowed to target any players with these commands. A player must consent to being targeted by `goto/call` by using the [`nogoto`](client/client_commands.md/#nogoto) and [`nocall`](client/client_commands.md/#nocall)
```

---

## Chat features
The chat in ETJump offers a lot of new features. You can add timestamps to chat messages, expand it to show more than **8** messages, change the size and position and move it around freely.

The chat also supports a mentioning systen. You can tag players by typing a part of their name inside at signs, e.g. `@name@`. This marks the chat message for the tagged client and plays a notification sound.

THe full list of customization available is the following.

* [`etj_chatAlpha`](client/etjump_cvars.md/#etj_chatalpha)
* [`etj_chatBackgroundAlpha`](client/etjump_cvars.md/#etj_chatbackgroundalpha)
* [`etj_chatFlags`](client/etjump_cvars.md/#etj_chatflags)
* [`etj_chatLineWidth`](client/etjump_cvars.md/#etj_chatlinewidth)
* [`etj_chatPosX`](client/etjump_cvars.md/#etj_chatposx), [`etj_chatPosY`](client/etjump_cvars.md/#etj_chatposy)
* [`etj_chatScale`](client/etjump_cvars.md/#etj_chatscale)
* [`etj_chatShadow`](client/etjump_cvars.md/#etj_chatshadow)
* [`etj_drawMessageTime`](client/etjump_cvars.md/#etj_drawmessagetime)
* [`etj_highlight`](client/etjump_cvars.md/#etj_highlight)
* [`etj_highlightSound`](client/etjump_cvars.md/#etj_highlightsound)
* [`etj_highlightText`](client/etjump_cvars.md/#etj_highlighttext)

---

## Private messages
You can send private messages to other players by typing `/m <name|clientnum> <message>` in the console.

```{note}
Private messages are sent to all players who's name match `<name>` partially. If you want to make sure you're only sending the message to a single client, it's safer to use `<clientnum>`.
```

---

## HUD drawing
A lot of the standard HUD elements are not important while playing ETJump, and can be hidden with the following cvars.

* [`etj_HUD_chargeBar`](client/etjump_cvars.md/#etj_hud_chargebar)
* [`etj_HUD_fatigueBar`](client/etjump_cvars.md/#etj_hud_fatiguebar)
* [`etj_HUD_fireteam`](client/etjump_cvars.md/#etj_hud_fireteam)
* [`etj_HUD_healthBar`](client/etjump_cvars.md/#etj_hud_healthbar)
* [`etj_HUD_playerHead`](client/etjump_cvars.md/#etj_hud_playerhead)
* [`etj_HUD_playerHealth`](client/etjump_cvars.md/#etj_hud_playerhealth)
* [`etj_HUD_popup`](client/etjump_cvars.md/#etj_hud_popup)
* [`etj_HUD_weaponIcon`](client/etjump_cvars.md#etj_hud_weaponicon)
* [`etj_HUD_xpInfo`](client/etjump_cvars.md/#etj_hud_xpinfo)

---

## Portal gun
ETJump includes a portalgun for players to use. It can be found in `weaponbank 9`. Firing the secondary portal is done with `+attack2` instead of `weapalt`.

```{tip}
To ease the portalgun usage, you can use [`etj_autoPortalBinds`](client/etjump_cvars.md/#etj_autoportalbinds) cvar.
```

```{note}
Depending on the map and server settings, portalgun might be disabled, as it's quite exploitable on a lot of maps.
```
