import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = []
for _ in range(N):
    l = int(input().rstrip())
    lst.append(l)
lst.sort(reverse=True)

dap = 0
for i in range(N-2):
    if lst[i] < lst[i+1]+lst[i+2]:
        print(lst[i]+lst[i+1]+lst[i+2])
        break
else:
    print(-1)