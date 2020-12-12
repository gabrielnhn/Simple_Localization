#!/usr/bin/env python3
import math
import numpy as np
from random import randrange
from map_module import Map
import cv2 as cv


# Map settings:
ROWS = 100
COLUMNS = 100
NUM_LANDMARKS = 5

# Plotting a map $magnitude times bigger than the matrix:
magnitude = 8

# Make new random map
map = Map(ROWS, COLUMNS, NUM_LANDMARKS)

# Place the robot in the map (in an available cell)
ROBOT_SYMBOL = '@'
has_placed_robot = False

while not has_placed_robot:
    # Get random coordinate
    i = randrange(map.rows)
    j = randrange(map.columns)

    # Try to place the robot
    if map.matrix[i, j] == map.EMPTY:
        map.matrix[i, j] = ROBOT_SYMBOL
        robot_coord = (j, i) # width, height coordinates
        has_placed_robot = True

# Equation coefficients
def coefficients(robotDistToLandmarks, landmarks, l0, l1):
    indepCoefficient = robotDistToLandmarks[l0] **2 - robotDistToLandmarks[l1] **2
    indepCoefficient -= (landmarks[l0][0] **2 + landmarks[l0][1] **2)
    indepCoefficient += (landmarks[l1][0] **2 + landmarks[l1][1] **2)
    indepCoefficient /= 2
    aCoefficient = landmarks[l1][0] - landmarks[l0][0]
    bCoefficient = landmarks[l1][1] - landmarks[l0][1]
    return [aCoefficient, bCoefficient, indepCoefficient]


if __name__ == "__main__":

    picture = map.get_picture(magnitude=magnitude,  negated=1)

    robx, roby = robot_coord

    robotDistToLandmarks = []
    landmarks = []

    for ID, landmark in map.landmarks:
        # For each landmark, compute the distance between itself and the robot
        
        # Get landmark position
        landx, landy = landmark

        # Store the distance
        diffPoints = np.subtract(landmark, robot_coord)
        robotDistToLandmarks.append(math.hypot(diffPoints[0],diffPoints[1]))
        # Store the landmark itself (without the ID)
        landmarks.append(landmark)

        # Plot the distance 
        cv.line(picture, (robx * magnitude, roby * magnitude), (landx*magnitude, landy*magnitude), (255,0,0))
    
    # Make system of equations to get the robot's position
    firstCoefficients = coefficients(robotDistToLandmarks, landmarks, 0, 1)
    secondCoefficients = coefficients(robotDistToLandmarks, landmarks, 0, 2)
    
    a = np.array([firstCoefficients[:2],secondCoefficients[:2]])
    b = np.array([firstCoefficients[2], secondCoefficients[2]])

    # Solve the system
    position = list(np.linalg.solve(a,b))
    print(position)
    

    # Get the coordinate to plot the robot (in the augmented map)
    position_in_picture = []
    for i in position:
        position_in_picture.append(magnitude * int(i)) 

    # Plot the robot's position
    cv.circle(picture, tuple(position_in_picture), magnitude, (0,255,0), cv.FILLED)

    # Show the map
    cv.imshow('map', picture)
    #cv.imwrite('map5.png', new_pic)
    cv.waitKey(0)