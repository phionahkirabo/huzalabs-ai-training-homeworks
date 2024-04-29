def alternatingSum(L):
    if not L:  
        return 0
    elif len(L) == 1:  
        return L[0]
    else:
        
        return L[0] - alternatingSum(L[1:])
