import sys
input = sys.stdin.readline
N = int(input().rstrip())
for _ in range(N):
    s = float(input())
    print(f'${s*0.8:.2f}')