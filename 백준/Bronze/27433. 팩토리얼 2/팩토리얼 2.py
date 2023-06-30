import sys
input = sys.stdin.readline
N = int(input().rstrip())

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

print(fact(N))