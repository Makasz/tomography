import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

SOURCE_DIR = "./source/"
FINAL_DIR = "./final/"


def PointsInCircum(r, n, c):
    return [(np.cos(2*np.pi/n*x)*r + c, np.sin(2*np.pi/n*x)*r + c) for x in range(n+1)]


def line(img, x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    if dx > dy:
        err = dx / 2.0
        while x != x1:
            try:
                img[int(x)][int(y)] = 127
            except:
                pass
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            try:
                img[int(x)][int(y)] = 127
            except:
                pass
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    try:
        img[int(x)][int(y)] = 127
    except:
        pass
    return img


if __name__ == "__main__":
    pass



for filename in os.listdir(SOURCE_DIR):
    print("Processing file " + filename)
    img = cv2.imread(SOURCE_DIR + filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_len = len(img)
    points = PointsInCircum(200, 32, img_len/2)
    for p in points:
        print("Drawing line to " + str(p))
        img = line(img, int(p[0]), int(p[1]), int(img_len/2), int(img_len/2))

    cv2.imwrite(FINAL_DIR + filename, img)
