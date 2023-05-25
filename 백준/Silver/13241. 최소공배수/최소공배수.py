import sys
input = sys.stdin.readline
def GCD(x,y):
    while y:
        x, y = y, x%y
    return x
A, B = map(int, input().rstrip().split())
print(A*B//GCD(A,B))