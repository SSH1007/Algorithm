N = int(input())
arr = ['*', ' ']
for n in range(1, N+1):
    print(' '*(N-n), '* '*n, sep = '')