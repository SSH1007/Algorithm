import sys
input = sys.stdin.readline
N = int(input().rstrip())
dap = 0
for _ in range(N):
    score = list(map(int, input().rstrip().split()))
    run = score[:2]
    trick = score[2:]
    runMax = max(run)
    trickSum = sum(sorted(trick, reverse=True)[:2])
    if dap < runMax + trickSum:
        dap = runMax + trickSum
print(dap)