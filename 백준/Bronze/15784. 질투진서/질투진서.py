import sys
input = sys.stdin.readline
N, a, b = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
jinseo = graph[a-1][b-1]
for n in range(N):
    if graph[n][b-1] > jinseo:
        print('ANGRY')
        exit(0)
    if n == a-1:
        for m in range(N):
            if graph[n][m] > jinseo:
                print('ANGRY')
                exit(0)
else:
    print('HAPPY')