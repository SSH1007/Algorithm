# 백준 15681 트리와 쿼리
# 트리 DP <- DFS를 visit 체크를 풀어주지 않으면서 진행
# 재귀횟수 초과 문제 때문에 setrecursionlimit 설정
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)


def main():
    N, R, Q = map(int, input().split())
    # 트리 생성
    tree = [[] for _ in range(N+1)]
    # 서브트리는 아무리 작더라도 자신의 루트를 포함하고 있으므로
    # 서브트리의 정점의 수를 나타내는 dp의 초기값은 1
    dp = [1]*(N+1)
    for _ in range(N-1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    # 방문 리스트 초기화
    visited = [False]*(N+1)

    def DFS(cur):
        visited[cur] = True
        for node in tree[cur]:
            if not visited[node]:
                dp[cur] += DFS(node)
        return dp[cur]

    DFS(R)

    for _ in range(Q):
        print(dp[int(input())])


if __name__ == '__main__':
    main()