def getInRange(x, bound1, bound2):
    lower_bound = min(bound1, bound2)
    upper_bound = max(bound1, bound2)

    if x < lower_bound:
        return lower_bound
    elif x > upper_bound:
        return upper_bound
    else:
        return x

print(getInRange(1, 3, 5))  
print(getInRange(4, 3, 5))  
print(getInRange(6, 3, 5))  
print(getInRange(6, 5, 3)) 
