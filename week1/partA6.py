def getKthDigit(n, k):
   
    n = abs(n)

   
    n_str = str(n)

    
    index = len(n_str) - k - 1

 
    if index >= 0 and index < len(n_str):
      
        return int(n_str[index])
    else:
        
        return 0


print(getKthDigit(789, 0)) 
print(getKthDigit(789, 1))  
print(getKthDigit(789, 2))    
print(getKthDigit(789, 3))
print(getKthDigit(-789, 0))  
