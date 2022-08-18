N = int(input())
for n in range(1, N+1):
    if n%2:
        print('* '*N)
    else:
        print(' *'*N)
