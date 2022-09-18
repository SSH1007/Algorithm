N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
dap = 64
for m in range(M-7):    
    for n in range(N-7):
        #Bstart : (0,0)이 B일때, 바꿔야 하는 개수
        #Wstart : (0,0)이 W일때, 바꿔야 하는 개수
        Bstart,Wstart = 0,0 
        for x in range(n,n+8):
            for y in range(m,m+8):
                if (x+y)%2:
                    if lst[x][y] == 'B':
                        Wstart+=1
                    else:
                        Bstart+=1
                else:
                    if lst[x][y] == 'B':
                        Bstart+=1
                    else:
                        Wstart+=1
        if dap > min(Bstart,Wstart):
            dap = min(Bstart, Wstart)
print(dap)