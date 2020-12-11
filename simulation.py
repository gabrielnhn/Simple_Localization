#!/usr/bin/env python3
import math
import numpy as np
from random import randrange
from map_module import Map
import cv2 as cv

# magnitude para imprimir um mapa maior
magnitude = 8

# Cria um mapa com landmarks aleatorios
map = Map()
ROBOT = '@'

# Poe o Robo no mapa
has_placed_robot = False
while not has_placed_robot:
    i = randrange(map.rows)
    j = randrange(map.columns)

    if map.matrix[i, j] == map.EMPTY:
        map.matrix[i, j] = ROBOT
        robot_coord = (j, i) # width, height coordinates
        has_placed_robot = True

# Coeficientes da equação
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
    # Tentamos criar mais uma dimensao pra imagem ficar em BGR, mas falhamos
    new_pic = picture[..., np.newaxis]

    robx, roby = robot_coord

    robotDistToLandmarks = []
    landmarks = []

    for ID, landmark in map.landmarks:
        # Pra cada landmark no mapa, calcula a distancia entre ela e o robo
        landx, landy = landmark
        cv.line(new_pic, (robx * magnitude, roby * magnitude), (landx*magnitude, landy*magnitude), (0,0,255))
        
        diffPoints = np.subtract(landmark, robot_coord)

        robotDistToLandmarks.append(math.hypot(diffPoints[0],diffPoints[1]))
        landmarks.append(landmark)
    
    # Cria um sistema de equacoes para obter a posicao do robo
    firstCoefficients = coefficients(robotDistToLandmarks, landmarks, 0, 1)
    secondCoefficients = coefficients(robotDistToLandmarks, landmarks, 0, 2)

    a = np.array([firstCoefficients[:2],secondCoefficients[:2]])
    b = np.array([firstCoefficients[2], secondCoefficients[2]])

    # Resolve o sistema
    pose = list(np.linalg.solve(a,b))
    
    # Trata a pose para obter sua posicao na imagem
    for i in range(len(pose)):
        pose[i] = magnitude * int(pose[i])
 
    print(pose)

    # Plota a pose na imagem
    cv.circle(new_pic, tuple(pose), magnitude, (0,255,0), cv.FILLED)

    # Exibe a imagem
    cv.imshow('map', new_pic)
    # cv.imwrite('results/map5.png', new_pic)
    cv.waitKey(0)