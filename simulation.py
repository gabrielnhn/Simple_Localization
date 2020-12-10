#!/usr/bin/env python3
import numpy as np
# Let's print the whole matrix
np.set_printoptions(threshold=np.inf)

import map_module

map = map_module.new_map(map_module.rows, map_module.columns,
                         map_module.landmarks_count)

print(map)