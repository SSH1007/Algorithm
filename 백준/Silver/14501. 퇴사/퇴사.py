import sys
input = sys.stdin.readline
N = int(input().rstrip())
# 최대 수익을 구할 dp 초기화
schedule = [0 for _ in range(N+1)]
# 상담 정보(기간, 보수)
info = []
# N일 동안의 상담 정보 입력
for _ in range(N):
    T, P = map(int, input().rstrip().split())
    info.append([T,P])

for i in range(N):
    for j in range(i+info[i][0], N+1):
        if schedule[j] < schedule[i]+info[i][1]:
            schedule[j] = schedule[i]+info[i][1]
print(schedule[-1])