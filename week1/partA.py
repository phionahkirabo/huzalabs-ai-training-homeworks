import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1 = 1
y1 = 2
x2 = 4
y2 = 6
print("Distance between points:", distance(x1, y1, x2, y2))