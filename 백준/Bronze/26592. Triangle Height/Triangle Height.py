import sys
input = sys.stdin.readline
n = int(input().rstrip())
for _ in range(n):
    a, b = map(float, input().rstrip().split())
    print(f'The height of the triangle is {(2*a)/b:.2f} units')