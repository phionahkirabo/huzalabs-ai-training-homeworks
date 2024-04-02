def roundHalfUp(n):
    return int(n + 0.5)

def colorBlender(rgb1, rgb2, midpoints, n):
  
    r1 = rgb1 // 1000000
    g1 = (rgb1 // 1000) % 1000
    b1 = rgb1 % 1000

  
    r2 = rgb2 // 1000000
    g2 = (rgb2 // 1000) % 1000
    b2 = rgb2 % 1000

    
    r_step = (r2 - r1) / (midpoints + 1)
    g_step = (g2 - g1) / (midpoints + 1)
    b_step = (b2 - b1) / (midpoints + 1)

   
    r = roundHalfUp(r1 + r_step * n)
    g = roundHalfUp(g1 + g_step * n)
    b = roundHalfUp(b1 + b_step * n)

    
    return r * 1000000 + g * 1000 + b


print(colorBlender(220020060, 189252201, 3, 1)) 