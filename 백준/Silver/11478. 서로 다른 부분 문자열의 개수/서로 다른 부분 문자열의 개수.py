import sys
input = sys.stdin.readline
S = input().rstrip()
dap = set()
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        dap.add(S[i:j])
print(len(dap))