import sys
input = sys.stdin.readline
N = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
dap = 0
for g in graph:
    dap += sum(g)
print(dap)