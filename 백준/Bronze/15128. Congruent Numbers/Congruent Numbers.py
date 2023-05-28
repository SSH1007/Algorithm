import sys
input = sys.stdin.readline
p1, q1, p2, q2 = map(int, input().rstrip().split())
dap = p1*p2/q1/q2/2
print(0 if dap%1 else 1)