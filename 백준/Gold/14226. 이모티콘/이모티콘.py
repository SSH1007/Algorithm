from collections import deque


S = int(input())
q = deque([(1, 0, 0)])
dic = dict()
dic[(1, 0, 0)] = 1


def BFS():
    while q:
        e, c, t = q.popleft()
        if e == S:
            print(t)
            break
        if not dic.get((e, e, t+1)):
            q.append((e, e, t+1))
            dic[(e, e, t+1)] = 1
        if c>0 and not dic.get((e+c, c, t+1)):
            q.append((e+c, c, t+1))
            dic[(e+c, c, t+1)] = 1
        if e>0 and not dic.get((e-1, c, t+1)):
            q.append((e-1, c, t+1))
            dic[(e-1, c, t+1)] = 1


BFS()