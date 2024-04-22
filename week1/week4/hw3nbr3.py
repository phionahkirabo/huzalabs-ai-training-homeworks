def getPairSum(L, target):
    num_set = set()
    for num in L:
        complement = target - num
        if complement in num_set:
            return (complement, num)
        num_set.add(num)
    return None

# Test cases
print(getPairSum([1], 1))  # None
print(getPairSum([5, 2], 7))  # (5, 2) or (2, 5)
print(getPairSum([10, -1, 1, -8, 3, 1], 2))  # (-1, 3) or (3, -1)
print(getPairSum([10, -1, 1, -8, 3, 1], 10))  # None
