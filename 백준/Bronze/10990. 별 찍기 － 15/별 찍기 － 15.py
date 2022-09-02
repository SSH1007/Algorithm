N = int(input())
print((N-1)*' ','*',sep='')
if N > 1:
    for n in range(1, N):
        print((N-1-n)*' ','*',(2*n-1)*' ','*',sep='')