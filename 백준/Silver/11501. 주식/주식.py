import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    lst = list(map(int, input().rstrip().split()))
    dap, maxV = 0, lst[-1]
    for i in range(N-1, -1, -1):
        if lst[i] > maxV:
            maxV = lst[i]
        else:
            dap += (-lst[i]+maxV)
    print(dap)