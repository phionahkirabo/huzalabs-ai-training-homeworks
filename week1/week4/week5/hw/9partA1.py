def oddCount(L):
    if not L:  
        return 0
    else:
        if L[0] % 2 != 0:  
            return 1 + oddCount(L[1:])  
        else:
            return oddCount(L[1:])  
