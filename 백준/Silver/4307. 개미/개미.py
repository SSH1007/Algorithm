import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    l, n = map(int, input().rstrip().split())
    fastT, slowT = 0, 0
    for _ in range(n):
        ant = int(input().rstrip())
        fastT = max(fastT, min(ant, l-ant))
        slowT = max(slowT, ant, l-ant)
    print(fastT, slowT)