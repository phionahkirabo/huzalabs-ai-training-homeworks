def containsPythagoreanTriple(L):
    squared_set = set(num ** 2 for num in L)
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[i] ** 2 + L[j] ** 2 in squared_set:
                return True
    return False

# Test cases
print(containsPythagoreanTriple([1, 3, 6, 2, 5, 1, 4]))  # True
print(containsPythagoreanTriple([1, 3, 6, 2, 1, 4]))     # False
