while 1:
    start, by, goal = map(int, input().split())
    if start == by == goal == 0:
        break
    tmp = goal-start+by
    if tmp%by or (by and start > goal):
        print('X')
    else:
        print(tmp//by)