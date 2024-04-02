def eggCartons(eggs):
    cartons = eggs // 12  
    if eggs % 12 != 0:    
        cartons += 1     
    return cartons


print(eggCartons(24))  
print(eggCartons(25))  
print(eggCartons(12))  
print(eggCartons(0))   
