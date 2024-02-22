import sys
input = sys.stdin.readline
N = int(input().rstrip())
points = []
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    points.append((x, y))
dap = 0
distance = []
for j in range(1, N):
    distance.append(abs(points[j][0]-points[j-1][0]) + abs(points[j][1]-points[j-1][1]))

minus = 0
for i in range(1, N-1):
    passPoint = abs(points[i+1][0]-points[i-1][0]) + abs(points[i+1][1]-points[i-1][1])
    checkPoint = abs(points[i][0]-points[i-1][0]) + abs(points[i][1]-points[i-1][1]) + abs(points[i+1][0]-points[i][0]) + abs(points[i+1][1]-points[i][1])
    minus = max(minus, abs(passPoint-checkPoint))
print(sum(distance)-minus)