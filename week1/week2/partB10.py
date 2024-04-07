def carrylessAdd(x, y):
    result = 0
    power = 0

  
    while x > 0 or y > 0:
       
        digit_x = x % 10
        digit_y = y % 10
        
        
        sum_digits = (digit_x + digit_y) % 10
        
        
        result += sum_digits * (10 ** power)
        
        
        x //= 10
        y //= 10
        power += 1

    return result


print(carrylessAdd(785, 376))  
