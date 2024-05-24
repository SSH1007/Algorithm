import sys
input = sys.stdin.readline
N = int(input().rstrip())
S = list(map(int, input().rstrip().split()))
visited = [0]*(sum(S)+2)


def DFS(idx, hap):
    if idx == N:
        return
    hap += S[idx]
    visited[hap] = 1
    DFS(idx+1, hap-S[idx])
    DFS(idx+1, hap)


DFS(0, 0)
print(visited[1:].index(0)+1)