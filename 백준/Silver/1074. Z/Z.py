# 좌표평면
# 2 1
# 3 4
N, r, c = map(int, input().split())
std = 0
dap = 0
while N>0:
    # 사분면 기준은 2의 N-1 승
    std = 2**(N-1)
    # 2사분면
    if r<std and c<std:
        pass
    # 1사분면
    if r<std and c>=std:
        dap+= 2**(N-1)*2**(N-1)
        c-=std
    # 3사분면
    if r>=std and c<std:
        dap+= 2**(N-1)*2**(N-1)*2
        r-=std
    # 4사분면 
    if r>=std and c>=std:
        dap+= 2**(N-1)*2**(N-1)*3
        r-=std
        c-=std

    N-=1
print(dap)