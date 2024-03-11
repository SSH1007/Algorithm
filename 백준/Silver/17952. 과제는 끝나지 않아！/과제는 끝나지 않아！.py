import sys
input = sys.stdin.readline
N = int(input().rstrip())
score = 0
stack = []
for _ in range(N):
    info = list(input().rstrip().split())
    if info[0] == '1':
        if int(info[2])-1 == 0:
            score += int(info[1])
        else:
            stack.append([int(info[1]), int(info[2])-1])
    else:
        if stack:
            data = stack.pop()
            data[1] -= 1
            if data[1] == 0:
                score += data[0]
            else:
                stack.append([data[0], data[1]])
        else:
            continue
print(score)