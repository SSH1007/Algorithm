N, M, K = map(int,input().split())
a = [M, K]
b = [N-M, N-K]
print(min(a)+min(b))