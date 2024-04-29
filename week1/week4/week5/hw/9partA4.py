def maxOdd(L):
    if not L:  
        return None
    else:
        if L[0] % 2 != 0:  
            max_rest = maxOdd(L[1:])  
            if max_rest is None or L[0] > max_rest:  
                return L[0]  
            else:
                return max_rest  
            return maxOdd(L[1:])  