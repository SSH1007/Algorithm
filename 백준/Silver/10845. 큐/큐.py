import sys
input = sys.stdin.readline
N = int(input())
que = []
for _ in range(N):
    command = list(input().split())
    if len(command)>1:
        # push
        que.append(command[1])
    else:
        if command[0] == 'pop':
            if que:
                print(que.pop(0))
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