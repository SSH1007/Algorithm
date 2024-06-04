import sys
input = sys.stdin.readline
# 아이들 수 N, 보석 색깔 수 M (1 ≤ N ≤ 10^9, 1 ≤ M ≤ 300, 000, M ≤ N)
N, M = map(int, input().rstrip().split())
gem = []
for _ in range(M):
    gem.append(int(input().rstrip()))


def ceil(x):
    if x % 1:
        return int(x)+1
    else:
        return int(x)


def fn(x):
    if x == 0:
        return False
    # 최소값을 찾는 것이므로 매개변수가 조건을 만족하면
    # True를 반환하는 것으로 검사범위를 x보다 작은 쪽으로 설정
    cnt = 0
    for g in gem:
        cnt += ceil(g/x)
    if cnt <= N:
        return True
    else:
        return False


l, r = 0, max(gem)
dap = int(1e9)
while l <= r:
    # 매개변수
    p = (l+r)//2
    if fn(p):
        r = p-1
        dap = min(dap, p)
    else:
        l = p+1
print(dap)