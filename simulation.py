#!/usr/bin/env python3
import numpy as np
from random import randrange
from map_module import Map
import cv2

# Cria o mapa
map = Map()
ROBOT = '@'

# Poe o Robo no mapa
has_placed_robot = False
while not has_placed_robot:
    i = randrange(map.rows)
    j = randrange(map.columns)

    if map.matrix[i, j] == map.EMPTY:
        map.matrix[i, j] = ROBOT
        has_placed_robot = True

print("showing")
map.show_picture(negated=1)
