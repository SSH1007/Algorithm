import sys
input = sys.stdin.readline
T = int(input().rstrip())
for t in range(1, T+1):
    N = int(input().rstrip())
    A, B = map(int, input().rstrip().split())
    for _ in range(N):
        u, v = map(int, input().rstrip().split())
    print(f'Material Management {t}')
    print('Classification ---- End!')