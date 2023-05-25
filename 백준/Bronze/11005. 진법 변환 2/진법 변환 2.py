import sys
input = sys.stdin.readline
N, B = map(int, input().rstrip().split())
notations = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dap = ''
while N > 0:
    dap += notations[N%B]
    N = N//B
print(dap[::-1])