N = int(input())
for _ in range(N):
    x1, y1, floor1, x2, y2, floor2 = map(int, input().split())
    print(floor1+floor2+abs(x1-x2)+abs(y1-y2))