A, B, C, N = map(int, input().split())
def f():
    for a in range(0,N+1,A):
        for b in range(0,N+1,B):
            for c in range(0,N+1,C):
                if a+b+c==N:
                    return 1
    return 0
print(f())