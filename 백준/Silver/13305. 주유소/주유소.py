import sys
input = sys.stdin.readline
N = int(input().rstrip())
roads = list(map(int, input().rstrip().split()))
price = list(map(int, input().rstrip().split()))
dap = 0
for i in range(len(roads)):
    if price[i] == min(price[i:-1]):
        dap += price[i]*sum(roads[i:])
        print(dap)
        sys.exit(0)
    else:
        dap += price[i]*roads[i]
print(dap)