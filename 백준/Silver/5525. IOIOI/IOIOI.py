import sys
input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())
S = input().rstrip()
start, end = 0, 2
dap = 0
for m in range(M):
    start = m
    end = start + 1+(N*2)
    if S[start:end] == 'I'+'OI'*N:
        dap += 1
        start+=2
        end+=2
    else:
        start+=1
        end+=1
print(dap)