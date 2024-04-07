def digitCount(n):
    
    if n == 0:
        return 1

    
    n = abs(n)

    count = 0
    while n > 0:
        n //= 10  
        count += 1

    return count


print(digitCount(12323))  
print(digitCount(0))      
print(digitCount(-111)) 
