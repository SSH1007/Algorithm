import sys
input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))
numbers.sort()
start, end = 0, N-1
dap = 0
while start < end:
    armor = numbers[start] + numbers[end]
    if numbers[start] + numbers[end] == M:
        dap += 1
        start += 1
        end -= 1
    elif numbers[start] + numbers[end] < M:
        start += 1
    else:
        end -= 1

print(dap)