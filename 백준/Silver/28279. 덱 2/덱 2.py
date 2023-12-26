import sys
input = sys.stdin.readline
from collections import deque
d = deque()
N = int(input().rstrip())
for _ in range(N):
    command = input().rstrip().split()
    if command[0] == '1':
        d.appendleft(int(command[1]))
    elif command[0] == '2':
        d.append(int(command[1]))
    elif command[0] == '3':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif command[0] == '4':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif command[0] == '5':
        print(len(d))
    elif command[0] == '6':
        if d:
            print(0)
        else:
            print(1)
    elif command[0] == '7':
        if d:
            print(d[0])
        else:
            print(-1)
    elif command[0] == '8':
        if d:
            print(d[-1])
        else:
            print(-1)