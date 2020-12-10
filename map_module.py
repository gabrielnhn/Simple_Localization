#!/usr/bin/env python3
"""
Makes a numpy.ndarray of a map with some landmarks
"""

import numpy as np
from random import randrange

rows = 100
columns = 100
landmarks_count = 10
EMPTY = "."
LANDMARK = "L"

def new_map(rows, columns, landmarks_count):
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