N, W, H = map(int, input().split())
C = (W**2+H**2)**0.5
for _ in range(N):
    l = int(input())
    if l <= W or l <= H or l <= C:
        print('DA')
    else:
        print('NE')