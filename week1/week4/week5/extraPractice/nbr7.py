import sys

def callWithLargeStack(f, *args):
    sys.setrecursionlimit(10000)
    return f(*args)

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def findRTP(digits):
    def backtrack(prefix):
        if len(prefix) == digits:
            return int(prefix)
        for digit in "123456789":
            candidate = int(prefix + digit)
            if isPrime(candidate) and backtrack(str(candidate)):
                return candidate
        return None

    return callWithLargeStack(backtrack, "")

# Test cases
print(findRTP(1))  # Example: 2
print(findRTP(2))  # Example: 23
print(findRTP(8))  # Example: 23399339
