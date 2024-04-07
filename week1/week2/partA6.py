def isRotation(x, y):
    
    x_str = str(x)
    y_str = str(y)

    
    if len(x_str) != len(y_str):
        return False

   
    y_str_rotation = y_str + y_str

   
    if x_str in y_str_rotation:
        return True
    else:
        return False


print(isRotation(1234, 3412))  
print(isRotation(1234, 2341))  
print(isRotation(1234, 1234))  
print(isRotation(1234, 4321))  
