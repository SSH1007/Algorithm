import sys
input = sys.stdin.readline
# 돈은 많고, 등수는 빠른게 좋지 않나?
N = int(input().rstrip())
line = []
for _ in range(N):
    line.append(int(input().rstrip()))
line.sort(key=lambda x: -x)

dap = 0

for n in range(N):
    tip = line[n] - n
    if tip > 0:
        dap += tip
print(dap)