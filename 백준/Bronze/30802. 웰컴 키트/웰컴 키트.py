N = int(input())
lst = list(map(int, input().split()))
A = 0
T, P = map(int, input().split())
for l in lst:
    A += l//T+1 if l%T else l//T
print(A)
print(N//P, N%P)