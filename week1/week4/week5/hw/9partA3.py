def oddsOnly(L):
    if not L:  
        return []
    else:
        if L[0] % 2 != 0:  
            return [L[0]] + oddsOnly(L[1:])  
        else:
            return oddsOnly(L[1:]) 