def numberOfPoolBallRows(balls):
    rows = 0
    total_balls = 0

    while total_balls < balls:
        rows += 1
        total_balls += rows

    return rows


print(numberOfPoolBallRows(6))   
print(numberOfPoolBallRows(7))   
print(numberOfPoolBallRows(15))  