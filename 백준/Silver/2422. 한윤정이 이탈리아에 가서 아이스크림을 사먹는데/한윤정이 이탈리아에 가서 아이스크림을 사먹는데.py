import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
answer = N*(N-1)*(N-2)//6
NoMatch = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    answer -= (N-2) - len(NoMatch[a-1] | NoMatch[b-1])
    # print(NoMatch)
    NoMatch[a-1].add(b)
    NoMatch[b-1].add(a)
print(answer)