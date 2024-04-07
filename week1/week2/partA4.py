def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def nthAdditivePrime(n):
    count = 0
    num = 2
    while True:
        if is_prime(num) and is_prime(sum_of_digits(num)):
            count += 1
            if count == n:
                return num
        num += 1


print(nthAdditivePrime(1))  
print(nthAdditivePrime(5))  
print(nthAdditivePrime(10)) 
