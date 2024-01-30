from collections import deque
N = int(input())
balloons = deque([(i+1, b) for i, b in enumerate(list(map(int, input().split())))])

while balloons:
    boom = balloons.popleft()
    print(boom[0], end=' ')
    if boom[1] > 0 and balloons:
        for _ in range(boom[1]-1):
            move = balloons.popleft()
            balloons.append(move)
    elif boom[1] < 0 and balloons:
        for _ in range(abs(boom[1])):
            move = balloons.pop()
            balloons.appendleft(move)