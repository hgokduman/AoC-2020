from AoC.Resource import Resource
from AoC import Display
import numpy as np

data = Resource(3).SplitLines().Get()

def toboggan(right, down):
    trees = 0
    posX, posY = [0, 0]

    while True:
        trees += 1 if data[posY][posX] == "#" else 0
        posX = (posX+right) % len(data[posY])
        posY += down
        if posY >= len(data):
            break
    return (trees)

def Day03(part=1):
    if part == 1:
        return (toboggan(3,1))
    elif part == 2:
        return(np.prod(list(map(toboggan, [1, 3, 5, 7, 1], [1, 1, 1, 1, 2]))))

Display.DisplayAnswers(Day03, [1, 2])