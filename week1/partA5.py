import math

def pascalsTriangleValue(row, col):
    
    if row < 0 or col < 0:
        return None


    if col > row:
        return None

    
    value = math.factorial(row) // (math.factorial(col) * math.factorial(row - col))

    return value


print(pascalsTriangleValue(0, 0))  
print(pascalsTriangleValue(3, 1))  
print(pascalsTriangleValue(5, 2))  
print(pascalsTriangleValue(-1, 2)) 
print(pascalsTriangleValue(4, -2)) 
print(pascalsTriangleValue(2, 5))  
