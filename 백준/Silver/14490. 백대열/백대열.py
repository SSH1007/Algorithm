N, M = map(int, input().split(':'))

def GCD (a, b):
    while b!=0:
        a, b = b, a%b
    return a

mom = GCD(N,M)
print(f'{N//mom}:{M//mom}')