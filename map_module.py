#!/usr/bin/env python3
"""
Makes a numpy.ndarray of a map with some landmarks
"""

import numpy as np
from random import randrange
import cv2 as cv
cv.namedWindow('map')

def new_map(rows, columns, landmarks_count, EMPTY, LANDMARK):
    """Makes a numpy.ndarray of a map with some landmarks"""
    # make map
    map = [[EMPTY for j in range(columns)] for i in range(rows)]
    map = np.array(map) # um pouco de eficiencia

    # insert landmarks
    landmarks = []
    for _ in range(landmarks_count):
        has_inserted = False
        while not has_inserted:
            i = randrange(rows)
            j = randrange(columns)

            if map[i, j] != LANDMARK: 
                map[i, j] = LANDMARK
                has_inserted = True
                landmarks.append((j, i))

    return map, landmarks


def print_map(map):
    str = ""
    for row in map:
        for char in row:
            str += char
        str += "\n"
    return str


class Map:
    rows = 100
    columns = 100
    landmarks_count = 10
    EMPTY = "-"
    LANDMARK = "X"
    
    def __init__(self):
        self.matrix, self.landmarks = new_map(self.rows, self.columns, self.landmarks_count,
                              self.EMPTY, self.LANDMARK)
    
    def __str__(self):
        return print_map(self.matrix)

    def get_picture(self, magnitude=8, negated=0):
        if negated:
            mask = np.ones((self.rows*magnitude, self.columns*magnitude))
        else:
            mask = np.zeros((self.rows*magnitude, self.columns*magnitude))

        mask = np.array(mask)

        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i, j] == self.LANDMARK:
                    mask[i*magnitude:i*magnitude+magnitude-1, j*magnitude:j*magnitude+magnitude-1] = 255 * (not negated)

        return mask