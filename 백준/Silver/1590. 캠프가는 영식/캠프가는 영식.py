import sys
input = sys.stdin.readline
# 버스의 개수 N과 영식이가 버스터미널에 도착하는 시간 T
N, T = map(int, input().rstrip().split())
dap = []
for _ in range(N):
    # 버스의 시작 시각 S, 간격 I, 버스 대수 C
    S, I, C = map(int, input().rstrip().split())
    # 버스 시간표 리스트 생성
    timestamp = [S+I*c for c in range(C)]
    # 만약 시간표의 마지막까지 가도 도착 시간 T에 다다를 수 없다면 그냥 넘긴다
    if timestamp[-1] < T:
        continue
    # 이분 탐색 시작
    start, end = 0, C-1
    point = 0
    while start <= end:
        mid = (start+end)//2
        # mid번째 버스 시간이 T와 같거나 크다면 point에 현재 mid 값을 저장해둔다.
        if timestamp[mid] >= T:
            point = mid
            end = mid - 1
        else:
            start = mid + 1
    dap.append(timestamp[point]-T)
print(min(dap) if dap else -1)