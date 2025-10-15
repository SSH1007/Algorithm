import sys
input = lambda: sys.stdin.readline().rstrip()
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    Z = a+b
    print(Z*Z*(Z-1)//2)