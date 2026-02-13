# Python Module dan Algoritma

import math

def jarak(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    return d

print("Jarak =", jarak (1, 2, 4, 6))