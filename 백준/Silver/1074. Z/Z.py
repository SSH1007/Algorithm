N, C, R = map(int, input().split())
dap = 0
def z(n,c,r):
    global dap
    # 사분면 판단 기중
    std = 2**(n-1)
    if n == 1:
        # Z 순서에 맞도록 숫자를 더함 
        dap += (2*(C%2)+(R%2))
        return 
    # 2사분면
    if c<std and r<std:
        pass
        z(n-1,c,r)
    # 3사분면
    elif c>=std and r<std:
        dap+=((std**2)*2)
        z(n-1,c-std,r)
    # 1사분면
    elif c<std and r>=std:
        dap+=(std**2)
        z(n-1,c,r-std)
    # 4사분면
    elif c>=std and r>=std:
        dap+=((std**2)*3)
        z(n-1,c-std,r-std)
z(N, C, R)
print(dap)