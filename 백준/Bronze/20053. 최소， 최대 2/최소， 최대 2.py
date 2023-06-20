T = int(input())
dap = []
for _ in range(T):
    N = int(input())
    lst = sorted(list(map(int, input().split())))
    dap.append((lst[0], lst[-1]))
for d in dap:
    print(*d)