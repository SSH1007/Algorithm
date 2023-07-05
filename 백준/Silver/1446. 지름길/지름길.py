import sys
input = sys.stdin.readline
N, D = map(int, input().rstrip().split())
dp = [i for i in range(D+1)]
shortcuts = []
for _ in range(N):
    s, e, d = map(int, input().rstrip().split())
    shortcuts.append((s, e, d))

# for 문으로 사용할 지름길 체크, if문으로 체크된 지름길에 맞게 갱신
for i in range(D+1):
    if i > 0:
        # 바로 전 위치와 비교하여 최소값으로 갱신
        dp[i] = min(dp[i-1]+1, dp[i])

    for s, e, d in shortcuts:
        # 도착위치가 고속도로의 길이를 넘어서면 pass
        if e > D:
            continue
        # 시작 위치에서 지름길만큼 간 거리가 도착위치보다 짧다면
        if s == i and dp[e] > dp[s]+d:
            # 도착위치를 지름길 기준으로 갱신
            dp[e] = dp[s]+d
print(dp[D])