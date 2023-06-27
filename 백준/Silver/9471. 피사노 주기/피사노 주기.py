import sys
input = sys.stdin.readline
P = int(input().rstrip())
daps = []
for _ in range(P):
    N, M = map(int, input().rstrip().split())
    fn = 1
    fnm = 1
    dap = 1
    while 1:
        tmp = (fn+fnm)%M
        fn = fnm
        fnm = tmp
        if fn == 1 and fnm == 1:
            break
        dap+=1
    daps.append((N, dap))
for d in daps:
    print(*d)