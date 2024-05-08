import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
# 인출금액이 충분한지로 이분탐색
budget = [int(input().rstrip()) for _ in range(N)]
# M번씩 인출할 금액 K의 최소와 최대 설정
s, e = min(budget), sum(budget)
dap = e
while s <= e:
    mid = (s+e)//2
    wallet = mid
    cnt = 1
    for b in budget:
        if wallet < b:  # 모자라면 다시 K(mid)원 인출
            wallet = mid
            cnt += 1
        wallet -= b
    # 인출금액 k가 최대 사용금액보다 작거나 인출횟수가 M보다 많으면(부족)
    if mid < max(budget) or cnt > M:
        s = mid+1
    # 인출금액 k가 하루를 보내기 충분할 경우
    else:
        e = mid-1
        dap = min(dap, mid)
print(dap)