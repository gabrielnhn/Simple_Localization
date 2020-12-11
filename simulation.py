#!/usr/bin/env python3
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
        robot_coord = (i, j)
        has_placed_robot = True

has_placed_goal = False
while not has_placed_goal:
    i = randrange(map.rows)
    j = randrange(map.columns)

    if map.matrix[i, j] == map.EMPTY:
        map.matrix[i, j] = GOAL
        goal_coord = (i, j)
        has_placed_goal = True

picture = map.get_picture(negated=1)
cv.imshow('map', picture)

print(picture.shape)

cv.waitKey(0)

def bfs(grid, start, goal, width, height):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

path = bfs(map.matrix, robot_coord, GOAL, map.columns, map.rows)

for grid in path:
    x, y = grid
    x, y = x * 8, y * 8
    cv.circle(picture, (x, y), 10, (0,0,255))

startx, starty = path[0]
endx, endy = path[-1]

cv.line(picture, (startx * 8, starty * 8), (endx*8, endy*8), (0,0,255))

cv.imshow('bgr', picture)
cv.waitKey(0)