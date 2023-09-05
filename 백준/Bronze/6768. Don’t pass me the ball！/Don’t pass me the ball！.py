import sys
input = sys.stdin.readline
J = int(input().rstrip())
dap = 0
for a in range(1, J+1):
    for b in range(a+1, J+1):
        for c in range(b+1, J+1):
            for d in range(c+1, J+1):
                if d >= J:
                    dap += 1
print(dap)