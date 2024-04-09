import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
bingo = [list(map(int, input().rstrip().split())) for _ in range(n)]
A = [''.join(map(str, b)).count('9') for b in bingo]
lotated = list(zip(*bingo))
B = [''.join(map(str, l)).count('9') for l in lotated]
if max(A) > max(B):
    print(sum(A)-max(A))
else:
    print(sum(B)-max(B))