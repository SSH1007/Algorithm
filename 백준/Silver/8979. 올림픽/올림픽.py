# 8979번 올림픽 : lambda 함수 정렬 사용법
import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
countries = [(list(map(int, input().rstrip().split()))) for _ in range(N)]
countries.sort(key=lambda x : (-x[1], -x[2], -x[3]))

index = [countries[i][0] for i in range(N)].index(K)
for i in range(N):
    if countries[i][1:] == countries[index][1:]:
        print(i+1)
        break
