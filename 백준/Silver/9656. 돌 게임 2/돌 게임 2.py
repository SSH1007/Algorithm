N = int(input())
dp = [0]*(N+1)
flag = True


def fibo(i):
    global flag
    flag = not flag
    if i < 0:
        return 0
    if i <= 1:
        return i
    if i > 3:
        return fibo(i-3)
    else:
        return fibo(i-1)


fibo(N)
if flag:
    print('SK')
else:
    print('CY')