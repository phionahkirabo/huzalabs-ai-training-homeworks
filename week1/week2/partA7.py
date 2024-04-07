def integral(f, a, b, N):
   
    h = (b - a) / N
    
   
    area = 0
    
   
    for i in range(N):
        x0 = a + i * h  
        x1 = a + (i + 1) * h  
        area += (f(x0) + f(x1)) * h / 2  
    
    return area


def f1(x): return x
def f2(x): return 2 * x + 3
def f3(x): return 2 * x ** 2

print(integral(f1, 0, 1, 10))  
print(integral(f2, 1, 2, 100))  
print(integral(f3, -1, 1, 1000))  
