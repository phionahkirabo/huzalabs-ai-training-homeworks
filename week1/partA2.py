import math

def circlesIntersect(x1, y1, r1, x2, y2, r2):
   
    distance_between_centers = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    
    if distance_between_centers <= r1 + r2:
        return True
    else:
        return False


x1 = 0
y1 = 0
r1 = 3
x2 = 4
y2 = 0
r2 = 2
print("Do the circles intersect?", circlesIntersect(x1, y1, r1, x2, y2, r2))