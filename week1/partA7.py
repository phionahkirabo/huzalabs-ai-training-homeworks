def setKthDigit(n, k, d):

    n_str = str(n)

    
    index = len(n_str) - k - 1

    
    if index >= 0 and index < len(n_str):
   
        n_str = n_str[:index] + str(d) + n_str[index + 1:]

       
        return int(n_str)
    else:
        
        return n


print(setKthDigit(468, 0, 1))  
print(setKthDigit(468, 1, 1))   
print(setKthDigit(468, 2, 1))  
print(setKthDigit(468, 3, 1))   
