# 8979번 올림픽 : lambda 함수 정렬 사용법
import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
countries = []
for _ in range(N):
    countries.append(list(map(int, input().rstrip().split())))
countries.sort(key=lambda x : (-x[1], -x[2], -x[3]))
index = 0
for n in range(N):
    if countries[n][0] == K:
        index = n
        break
for i in range(index):
    if countries[i][1:] == countries[index][1:]:
        print(i+1)
        break