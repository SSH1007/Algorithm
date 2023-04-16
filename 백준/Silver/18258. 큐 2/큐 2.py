import sys
input = sys.stdin.readline
N = int(input().rstrip())
from collections import deque
que = deque([])
for _ in range(N):
    command = list(input().rstrip().split())
    if command[0] == 'push':
        que.append(int(command[1]))
    elif command[0] == 'pop':
        if que:
            d = que.popleft()
            print(d)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(que))
    elif command[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)