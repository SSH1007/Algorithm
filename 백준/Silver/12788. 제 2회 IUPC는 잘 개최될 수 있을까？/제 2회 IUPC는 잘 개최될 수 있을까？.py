import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M, K = map(int, input().split())
As = sorted(list(map(int, input().split())), reverse=True)
tmp = 0
for n in range(N):
    tmp += As[n]
    if tmp >= M*K:
        print(n+1)
        break
else:
    print('STRESS')