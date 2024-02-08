N, M = map(int, input().split())
lecture = list(map(int, input().split()))
# 제일 긴 동영상 하나의 길이까지는 보장해야 하므로 블루레이의 최소 크기는 동영상 중 최댓값
# 동영상 모두를 한꺼번에 담는 게 블루레이 최대 크기
s, e = max(lecture), sum(lecture)
dap = 0
while s <= e:
    mid = (s+e)//2
    total = 0
    cnt = 1
    for l in lecture:
        total += l
        if total > mid:
            total = l
            cnt += 1
    # 블루레이의 수가 M보다 크다면 블루레이 수를 줄이기 위해 비교값을 늘려야 함
    if cnt > M:
        s = mid + 1
    else:
        dap = mid
        e = mid - 1
print(dap)