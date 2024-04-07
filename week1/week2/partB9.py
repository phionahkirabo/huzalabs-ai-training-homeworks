def findZeroWithBisection(f, x0, x1, epsilon):
    
    if f(x0) * f(x1) > 0:
        return None  
    
    
    while abs(x1 - x0) > epsilon:
        
        x_mid = (x0 + x1) / 2
        
        
        f_mid = f(x_mid)
        
        
        if abs(f_mid) < epsilon:
            return x_mid
        
        
        if f_mid * f(x0) < 0:
            x1 = x_mid
        else:
            x0 = x_mid
    
    
    return (x0 + x1) / 2


def f(x): return x ** 2 - 4  
x0 = 0  
x1 = 3  
epsilon = 0.0001  
root = findZeroWithBisection(f, x0, x1, epsilon)
print("Approximate root:", root)
print("Value of f at the root:", f(root))
