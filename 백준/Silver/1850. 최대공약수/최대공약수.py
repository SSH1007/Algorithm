import sys
input = sys.stdin.readline
A, B = map(int, input().rstrip().split())
# 111111 = 111 * 1001

def GCD(a, b):
    while b:
        a, b = b, a%b
    return a

print('1'*GCD(A,B))