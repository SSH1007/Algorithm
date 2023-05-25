import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
# 1. 모든 요청이 배정될 수 있는 경우, 요청한 금액 중 최댓값인 정수를 출력한다.
if sum(lst) <= M:
    print(max(lst))
# 2. 모든 요청이 배정될 수 없는 경우, 이분탐색으로 정수 상한액을 설정하여 배정한다.
else:
    start = 0
    end = max(lst)
    while start <= end:
        mid = (start+end)//2
        hap = 0
        for l in lst:
            hap += min(l, mid)
        if hap > M:
            end = mid-1
        else:
            start = mid+1
    print(end)