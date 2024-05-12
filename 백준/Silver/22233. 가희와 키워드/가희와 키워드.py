import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
memo = dict()
for _ in range(N):
    m = input().rstrip()
    memo[m] = 1
for _ in range(M):
    bs = list(input().rstrip().split(','))
    for b in bs:
        if b in memo.keys():
            del memo[b]
    print(len(memo))