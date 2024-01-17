M, N = map(int, input().split())
T = int(input())
store = []
for _ in range(T):
    dir, dist = map(int, input().split())
    if dir == 1:
        store.append((0, dist))
    elif dir == 2:
        store.append((N, dist))
    elif dir == 3:
        store.append((dist, 0))
    elif dir == 4:
        store.append((dist, M))

r, c = 0, 0
dn, de = map(int, input().split())
if dn == 1:
    r, c = 0, de
elif dn == 2:
    r, c = N, de
elif dn == 3:
    r, c = de, 0
elif dn == 4:
    r, c = de, M


dap = 0
for sr, sc in store:
    # 행이나 열끼리의 차가 N이나 M이라면 마주보고 있는 것
    if abs(sr-r) == N:
        dap += (min(N+sc+c, N+M-sc+M-c))
    elif abs(sc-c) == M:
        dap += (min(M+sr+r, M+N-sr+N-r))
    # 나머지는 ㄱ, ㄴ 위치
    else:
        dap += (abs(sr-r) + abs(sc-c))
print(dap)