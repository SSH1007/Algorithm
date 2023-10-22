while 1:
    start, by, goal = map(int, input().split())
    if start == by == goal == 0:
        break
    tmp = goal-start
    if tmp%by == 0 and tmp//by >= 0:
        print(tmp//by+1)
    else:
        print('X')