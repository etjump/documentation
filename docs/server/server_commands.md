# List of ETJump server commands
Below is a list of all ETJump related commands that the server or server admins can execute via rcon.

---

## dumpEntities

`dumpEntities [filename]`

Dumps all entities from the current map to a file. If `filename` isn't given, defaults to `mapname.ent`. The file will be dumped into `etjump/maps` directory.

This is effecticely the same as using the `-exportents` switch in `q3map2`, just more convenient by being able to do this directly in-game.

```{note}
Usage requires the map to be loaded with `developer 1` set.
```

```{tip}
* This produces an entity file that can be directly loaded by ET: Legacy and ETe servers to modify the entities present in a map, as an alternative to mapscripts.
* This can also be used to quickly dump an entity definition to be copied for mapscripting purposes.
```

---

## generateCustomvotes

`generateCustomvotes`

Generates a sample custom map vote file with the name specified in [`g_customMapVotesFile`](./server_cvars.md#g_custommapvotesfile).

---

## generateMotd

`generateMotd`

Generates a sample message of the day file.

---

## logstate

`logstate`

Logs the current state of the server, including client numbers, their current team and name.

```{hint}
The state is logged in the server log file.
```

---

## readCustomvotes

`readCustomvotes`

Reloads custom vote file specified in [`g_customMapVotesFile`](./server_cvars.md#g_custommapvotesfile).
