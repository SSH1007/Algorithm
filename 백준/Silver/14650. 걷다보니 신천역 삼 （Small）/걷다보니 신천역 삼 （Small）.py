N = int(input().rstrip())
dap = 0

def DFS(l, s):
    global dap
    if l == N:
        tmp = sum(map(int, s))
        if tmp % 3 == 0 and int(s) >= 10**(N-1):
            dap += 1
        return
    for i in ['0', '1', '2']:
        DFS(l+1, s+i)
DFS(0, '')
print(dap)