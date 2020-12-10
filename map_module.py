#!/usr/bin/env python3
"""
Makes a numpy.ndarray of a map with some landmarks
"""

import numpy as np
from random import randrange

def new_map(rows, columns, landmarks_count, EMPTY, LANDMARK):
    """Makes a numpy.ndarray of a map with some landmarks"""
    # make map
    map = [[EMPTY for j in range(columns)] for i in range(rows)]
    map = np.array(map) # um pouco de eficiencia

    # insert landmarks
    for _ in range(landmarks_count):
        has_inserted = False
        while not has_inserted:
            i = randrange(rows)
            j = randrange(columns)

            if map[i, j] != LANDMARK: 
                map[i, j] = LANDMARK
                has_inserted = True

    return map


def print_map(map):
    str = ""
    for row in map:
        for char in row:
            str += char
        str += "\n"
    return str


class Map:
    rows = 18
    columns = 18
    landmarks_count = 10
    EMPTY = "-"
    LANDMARK = "X"
    
    def __init__(self):
        self.matrix = new_map(self.rows, self.columns, self.landmarks_count,
                              self.EMPTY, self.LANDMARK)
    
    def __str__(self):
        return print_map(self.matrix)