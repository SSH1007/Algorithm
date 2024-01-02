import sys
input = sys.stdin.readline
N = int(input().rstrip())
price = []
for _ in range(N):
    price.append(int(input().rstrip()))
price.sort(reverse=True)

dap = 0
for i in range(0, N, 3):
    tmp = price[i:i+3]
    if len(tmp) == 3:
        dap += sum(tmp[:2])
    else:
        dap += sum(tmp)
print(dap)