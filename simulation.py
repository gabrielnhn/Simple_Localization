#!/usr/bin/env python3
import math
import numpy as np
from random import randrange
from map_module import Map
import cv2 as cv
import collections

# Cria o mapa
map = Map()
ROBOT = '@'
GOAL = '*'

# Poe o Robo no mapa
has_placed_robot = False
while not has_placed_robot:
    i = randrange(map.rows)
    j = randrange(map.columns)

    if map.matrix[i, j] == map.EMPTY:
        map.matrix[i, j] = ROBOT
        robot_coord = (j, i)
        has_placed_robot = True

# Main loop

while True:
    picture = map.get_picture(negated=1)
    
    robx, roby = robot_coord

    robotDistToLandmarks = list()


    for landmark in map.landmarks:
        landx, landy = landmark
        cv.line(picture, (robx * 8, roby * 8), (landx*8, landy*8), (0,0,255))
        
        diffPoints = np.subtract(landmark, robot_coord)

        robotDistToLandmarks.append(math.hypot(diffPoints[0],diffPoints[1]))

    print(robotDistToLandmarks)
        
    
    
    

    cv.imshow('bgr', picture)
    cv.waitKey(5)