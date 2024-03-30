N, L = map(int, input().split())
time = 0    # 총 소요 시간
former = 0     # 이전 신호등 위치 기록
for _ in range(N):
    D, R, G = map(int, input().split())
    time += (D-former)
    former = D
    cur = time % (R+G)
    if cur >= R:
        pass
    else:
        time += (R-cur)
print(time+L-former)