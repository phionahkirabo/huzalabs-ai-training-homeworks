def hasConsecutiveDigits(n):
    if n < 0: 
        return hasConsecutiveDigits(-n)
    elif n < 10:  
        return False
    else:
        last_digit = n % 10  
        second_last_digit = (n // 10) % 10  
        if last_digit == second_last_digit:  
            return True
        else:
            
            return hasConsecutiveDigits(n // 10)
