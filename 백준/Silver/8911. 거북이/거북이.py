T = int(input())
for _ in range(T):
    command = input()
    max_x, max_y, min_x, min_y = 0, 0, 0, 0
    x, y = 0, 0
    # 0 북 1 동 2 남 3 서
    dir = 0
    for c in command:
        if c == 'F':
            if dir == 0:
                y += 1
                max_y = max(max_y, y)
            elif dir == 1:
                x += 1
                max_x = max(max_x, x)
            elif dir == 2:
                y -= 1
                min_y = min(min_y, y)
            elif dir == 3:
                x -= 1
                min_x = min(min_x, x)
        elif c == 'B':
            if dir == 0:
                y -= 1
                min_y = min(min_y, y)
            elif dir == 1:
                x -= 1
                min_x = min(min_x, x)
            elif dir == 2:
                y += 1
                max_y = max(max_y, y)
            elif dir == 3:
                x += 1
                max_x = max(max_x, x)
        elif c == 'L':
            dir = (dir+1)%4
        elif c == 'R':
            dir = (dir-1)%4
    print((max_x-min_x)*(max_y-min_y))