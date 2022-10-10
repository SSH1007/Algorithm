import sys
input = sys.stdin.readline
# 최소 시간으로 땅고르기를 하고 그 경우 땅의 높이를 출력해라
# 위의 블록을 인벤토리에 넣는데 2초, 인벤토리에서 블록을 꺼내서 올려놓는데 1초
# 세로 N, 가로 M 크기의 집터. B는 작업 시작시 인벤토리 안의 블록 수
N, M, B = map(int, input().split())
terra = []
for _ in range(N):
    terra+=list(map(int, input().split()))

final_height, time = 0, float('inf')
min_h = min(terra)
max_h = max(terra)

# 높이의 개수(빈도) 목록
heights = [0]*(257)
for n in range(N*M):
    heights[terra[n]]+=1

for i in range(min_h, max_h+1):
    # 이미 있는 블록들과 인벤토리를 합쳐도 
    # 기준 i 높이로 평탄화된 구역보다 블록수가 적다면 작업 자체가 불가
    if i*(N*M) > sum(terra)+B:
        pass
    else:
        tmp_time = 0
        for h in range(len(heights)):
            if heights[h]:
                if h > i:   # 현재 높이가 기준 높이보다 높으면 퍼서 그 차이만큼 인벤토리에 담는다(2초씩)
                    tmp_time += ((h-i)*heights[h]*2)
                elif h < i: # 현재 높이가 기준 높이보다 낮으면 그 차이만큼 인벤토리에서 꺼낸다(1초씩)
                    tmp_time += ((i-h)*heights[h])
        if tmp_time <= time:
            time = tmp_time
            final_height = i
print(time, final_height)