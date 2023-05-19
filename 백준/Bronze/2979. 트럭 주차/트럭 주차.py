import sys
input = sys.stdin.readline
A, B, C = map(int, input().rstrip().split())
dap = 0
lst = [0]*100
for _ in range(3):
    a, b = map(int, input().rstrip().split())
    for i in range(a, b):
        lst[i] += 1
for i in range(100):
    if lst[i] == 1:
        dap += A
    elif lst[i] == 2:
        dap += (B*2)
    elif lst[i] == 3:
        dap += (C*3)
print(dap)