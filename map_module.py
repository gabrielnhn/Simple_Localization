#!/usr/bin/env python3
"""
Define map operations: create new map with random landmarks,
get a picture of the map, print the map as a matrix.
"""

__author__ = "Gabriel Hishida and Allan Cedric"

import numpy as np
from random import randrange
import cv2 as cv

def random_map(rows, columns, landmarks_count, EMPTY, LANDMARK):
    """Makes a numpy.ndarray of a map with random landmarks"""
    # make map
    map = [[EMPTY for j in range(columns)] for i in range(rows)]
    map = np.array(map) # um pouco de eficiencia

    # insert landmarks
    landmarks = []
    for count in range(landmarks_count):
        has_inserted = False
        while not has_inserted:
            i = randrange(rows)
            j = randrange(columns)

            if map[i, j] != LANDMARK: 
                map[i, j] = LANDMARK
                has_inserted = True
                landmarks.append((count, (j, i)))

    return map, landmarks


def get_string(map):
    """Get the map as a string"""
    str = ""
    for row in map:
        for char in row:
            str += char
        str += "\n"
    return str


class Map:
    """Map class"""
    rows = 100
    columns = 100
    landmarks_count = 5
    EMPTY = "-"
    LANDMARK = "X"
    
    def __init__(self):
        """Get a new random map"""
        self.matrix, self.landmarks = random_map(self.rows, self.columns, self.landmarks_count,
                              self.EMPTY, self.LANDMARK)
    
    def __str__(self):
        """Get the matrix as a string"""
        return get_string(self.matrix)

    def get_picture(self, magnitude=8, negated=0):
        """Get a numpy BGR matrix of the map, augmented $magnitude times"""
        mask = np.zeros((self.rows*magnitude, self.columns*magnitude, 3), dtype=np.uint8)
        mask.fill(255 * negated)
        print(mask)

        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i, j] == self.LANDMARK:
                    mask[i*magnitude:i*magnitude+magnitude-1, j*magnitude:j*magnitude+magnitude-1] = 255 * (not negated)

        return mask