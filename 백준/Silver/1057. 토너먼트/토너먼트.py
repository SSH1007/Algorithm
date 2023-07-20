N, A, B = map(int, input().split())
dap = 1
while N > 0:
    # 만약 참가자가 홀수면?
    if N % 2:
        N -= 1

    if A % 2:
        A = (A+1)//2
    else:
        A //= 2

    if B % 2:
        B = (B+1)//2
    else:
        B //= 2
       
    if A == B:
        print(dap)
        break

    N //= 2
    dap += 1