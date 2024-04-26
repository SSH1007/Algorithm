import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = []
for _ in range(N):
    Di, Ci = input().rstrip().split()
    lst.append((Di, int(Ci)))
J = 0
for l in lst:
    if l[0] =='jinju':
        J = l[1]
        print(J)
dap = 0
for l in lst:
    if l[1] > J:
        dap += 1
print(dap)