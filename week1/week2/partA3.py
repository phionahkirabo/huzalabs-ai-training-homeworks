def hasConsecutiveDigits(n):
    n = abs(n)  
    prev_digit = None
    while n > 0:
        digit = n % 10
        if prev_digit == digit:
            return True
        prev_digit = digit
        n //= 10
    return False


print(hasConsecutiveDigits(123))  
print(hasConsecutiveDigits(1223))  
print(hasConsecutiveDigits(-1223))  