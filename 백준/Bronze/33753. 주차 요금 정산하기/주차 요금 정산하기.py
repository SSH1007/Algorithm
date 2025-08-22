A, B, C = map(int, input().split())
T = int(input())
if T <= 30:
    print(A)
else:
    if (T-30)%B == 0:
        print(A+(T-30)//B*C)
    else:
        print(A+((T-30)//B+1)*C)