N = int(input())
if N%2 == 0:
    print('I LOVE CBNU')
else:
    t = N//2
    print('*'*N)
    print(' '*(N-t-1)+'*')
    for i in range(t):
        print(' '*(t-i-1)+'*'+' '*(2*i+1)+'*')