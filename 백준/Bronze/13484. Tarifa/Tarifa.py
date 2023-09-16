X = int(input())
N = int(input())
P = X
for _ in range(N):
    pi = int(input())
    P+=X
    P-=pi
print(P)