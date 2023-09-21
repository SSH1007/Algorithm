N, W, H = map(int, input().split())
for _ in range(N):
    x = int(input())
    if W**2+H**2 >= x**2 or W>=x or H>=x:
        print('YES')
    else:
        print('NO')