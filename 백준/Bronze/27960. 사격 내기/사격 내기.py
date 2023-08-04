target = [0]*10
A, B = map(int, input().split())


def func(N):
    for i in range(9,-1,-1):
        if N >= 2**i:
            N-=2**i
            target[i]+=1


func(A)
func(B)
dap = 0
for t in range(10):
    if target[t]==1:
        dap+=2**t
print(dap)