def nearestOdd(n):
  
    n_int = int(n)

 
    if n_int % 2 != 0:
       
        return n_int
    else:
       
        lower_odd = n_int - 1
        upper_odd = n_int + 1

   
        if abs(n_int - lower_odd) <= abs(n_int - upper_odd):
            return lower_odd
        else:
            return upper_odd


print(nearestOdd(13.0))    
print(nearestOdd(12.5))   
print(nearestOdd(11.6))    
print(nearestOdd(10))      