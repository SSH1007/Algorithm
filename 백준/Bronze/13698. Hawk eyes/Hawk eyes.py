YBW = input()
balls = [1,2,3,4]
for y in YBW:
    if y == 'A':
        balls[0], balls[1] = balls[1], balls[0]
    elif y == 'B':
        balls[0], balls[2] = balls[2], balls[0]
    elif y == 'C':
        balls[0], balls[3] = balls[3], balls[0]
    elif y == 'D':
        balls[1], balls[2] = balls[2], balls[1]
    elif y == 'E':
        balls[1], balls[3] = balls[3], balls[1]
    elif y == 'F':
        balls[2], balls[3] = balls[3], balls[2]
print(balls.index(1)+1)
print(balls.index(4)+1)