import sys
input = sys.stdin.readline
N = int(input().rstrip())
cnt, tmpSum = 0, 0
start, end = 0, 0
while end <= N:
    if tmpSum < N:
        end += 1
        tmpSum += end
    elif tmpSum > N:
        tmpSum -= start
        start += 1
    else:
        cnt += 1
        end += 1
        tmpSum += end
print(cnt)