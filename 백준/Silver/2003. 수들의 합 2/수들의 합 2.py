import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
start = 0
end = 1
dap = 0
while start < N and end < N+1:
    if sum(lst[start:end]) == M:
        dap+=1
        start+=1
    else:
        if sum(lst[start:end]) > M:
            start += 1
        else:
            end += 1
print(dap)