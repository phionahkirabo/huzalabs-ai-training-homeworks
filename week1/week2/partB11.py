def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

def digit_sum(n):
    return sum(map(int, str(n)))

def nthSmithNumber(n):
    smith_count = 0
    number = 4  

    while True:
        factors = prime_factors(number)
        if len(factors) > 1:  
            if digit_sum(number) == sum(map(digit_sum, factors)):
                smith_count += 1
                if smith_count == n:
                    return number
        number += 1


print(nthSmithNumber(1))  
print(nthSmithNumber(2))  
