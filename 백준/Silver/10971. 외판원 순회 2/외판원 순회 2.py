# 외판원 순회 = 비트마스킹, 백트래킹, dp
import sys
input = sys.stdin.readline
N = int(input().rstrip())
W = [list(map(int, input().rstrip().split())) for _ in range(N)]
inf = int(1e9)
# dp로 시간 복잡도를 줄이고, 비트마스킹으로 공간 복잡도 줄이기
# -1의 의미는 아직 미방문하여 비용이 미정이라는 뜻
dp = [[-1]*(1 << N) for _ in range(N)]
# 시작점 0은 이미 방문했다 (1<<0)
check = 1


def TSP(start, chk):
    # 전부 방문했다면
    if chk == (1 << N)-1:
        # 근데 시작점 0에 도달 못함
        if W[start][0] == 0:
            return inf
        # 도달했다면
        else:
            return W[start][0]

    # 이미 방문한 곳을 재방문한 경우
    if dp[start][chk] != -1:
        return dp[start][chk]   # start까지 방문한 최소 비용

    # dp[start][i]를 갱신하기 전에 dp[start][chk]를 inf로 초기화
    # (기존의 -1는 미방문을 의미. inf는 방문 시도했으나 접근 불가라는 의미)
    dp[start][chk] = inf
    # 시작점 0을 제외하고 1부터 방문
    for i in range(1, N):
        # W[same][same]은 방문 불가
        if W[start][i] == 0:
            continue
        # 이동하려는 시점에 이미 방문한 도시라면 패스
        if chk & (1 << i):
            continue
        dp[start][chk] = min(dp[start][chk], TSP(i, chk | (1 << i)) + W[start][i])

    return dp[start][chk]


print(TSP(0, check))