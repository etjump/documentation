# List of ETJump client commands
Below is a list of all available ETJump related console commands for players.

## backup
`backup [slot]`  
Loads a backup slot. Possible slots __1__-__3__. If no slot is given, loads slot __1__.

---

## call
`call [player]`  
Teleports target player to you.

---

## class
`class [class][weapon]`  
Changes to class with weapon. Possible classes are __s__, __e__, __m__, __f__, __c__. Possible weapons are __1__-__7__.

---

## god
`god`  
Toggles god mode.

---

## goto
`goto [player]`  
Teleports you to target player.

---

## incrementVar
`incrementVar [cvar] [start] [end] [step]`  
Cycles given cvar between values of `start` and `end` with increments of `step`. Same as `cycle`, but supports float values.

---

## interruptRun
`interruptRun`  
Interrupts a currently active timerun.

---

## iwant
`iwant [player]`  
Same as call.

---

## listinfo
`listinfo [map list]`  
Lists all callvote randommap map lists. If a map is given, lists the maps on the list.

---

## load
`load [slot]`  
Loads a previously saved position. Possible slots __0__-__2__. If no slot is given, loads slot __0__.

---

## manual
`manual [command]`  
Prints a manual for command.

---

## min and minimize
`min`, `minimize`  
Minimizes the ET client. Only works on windows.

---

## nocall
`nocall`  
Toggles whether other players are allowed to call you.

---

## noclip
`noclip`  
Toggles noclip.

---

## nogoto
`nogoto`  
Toggles whether other players can teleport to you.

---

## portal
`portal`  
Prints information about portal gun.

---

## ranks, records and times
`ranks [run name]`, `records [run name]`, `times [run name]`  
Prints top records in each run on the map. If a run name is given, prints top __50__ records on that run.

---

## save
`save [slot]`  
Saves current position. Possible slots __0__-__2__. If no slot is given, slot is __0__.

---

## setoffset
`setoffset [X Y Z]`  
Offsets your position by the amount of units on each vector. Usage requires access to `noclip`. Maximum offset value per vector is __4096__.