#!/usr/bin/env python3
import numpy as np
from random import randrange
import map_module

ROBOT = '@'

map = map_module.new_map()

has_placed_robot = False
while not has_placed_robot:
    i = randrange(map_module.rows)
    j = randrange(map_module.columns)

    if map[i, j] == map_module.EMPTY:
        map[i, j] = ROBOT
        has_placed_robot = True

map_module.print_map(map)