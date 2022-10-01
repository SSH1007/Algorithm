N, A, B, C, D = map(int, input().split())
X = N//A+(1 if N%A else 0)
Y = N//C+(1 if N%C else 0)
print(min(X*B, Y*D))