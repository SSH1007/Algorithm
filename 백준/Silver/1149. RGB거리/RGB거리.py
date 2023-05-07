import sys
input = sys.stdin.readline
N = int(input().rstrip())
house = []
# 빨초파로 칠하는 비용 house 리스트에 입력
for _ in range(N):
    R, G, B = map(int, input().rstrip().split())
    house.append([R,G,B])

# DP : N번째 빨간 집을 칠하는 비용은 N-1번째 초록, 파랑으로 칠하는 비용 중 최솟값과 N번째로 빨간색으로 칠하는 비용의 합이다
for i in range(1, N):
    house[i][0] += min(house[i-1][1], house[i-1][2])
    house[i][1] += min(house[i-1][0], house[i-1][2])
    house[i][2] += min(house[i-1][0], house[i-1][1])
print(min(house[N-1]))