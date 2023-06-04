import sys
input = sys.stdin.readline
while 1:
    S = input().rstrip()
    if S =='':
        break
    a, b, c = map(int, S.split())
    dap = max((b-a-1), (c-b-1))
    print(dap)