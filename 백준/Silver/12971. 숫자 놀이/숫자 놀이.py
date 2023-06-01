import sys
input =  sys.stdin.readline
P1, P2, P3, X1, X2, X3  = map(int, input().rstrip().split())
N = 0
while N <= P1*P2*P3:
    if N%P1 == X1 and N%P2 == X2 and N%P3 == X3:
        break
    N+=1
else:
    N = -1
print(N)