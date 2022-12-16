# 선수 수를 받고
N = int(input())
# 선수 명단 리스트 생성
lst = []
# 각 선수당 승점을 담을 딕셔너리 생성
winningPoints = dict()
# 선수마다 힘과 마술링의 힘을 받고 리스트와 딕셔너리에 각각 데이터 삽입
for i in range(N):
    power, magicPower = map(int, input().split())
    lst.append((power, magicPower))
    winningPoints[i] = 0
# 선수들끼리 대결
for i in range(N-1):
    for j in range(i, N):
        # 본인은 본인과 싸울 수 없다.
        if i==j:
            continue
        # 선수 A가 선수 B와 경기할 때,
        # A의 경기력 = A의 힘+B의 힘*A의 마술링의 힘
        Apower = lst[i][0]+lst[j][0]*lst[i][1] 
        Bpower = lst[j][0]+lst[i][0]*lst[j][1]
        # A와 B의 경기 결과에 따라 딕셔너리에 있는 해당 선수의 승 수를 더해준다(무승부는 고려 안함)
        if Apower > Bpower:
            winningPoints[i] += 1
        else:
            winningPoints[j] += 1

# 수여하는 금화 수를 최소화하기 위해서는 가장 많이 이긴 사람이 앞으로 가야 한다.(내림차순)
dap = sorted(winningPoints.items(), key = lambda x : x[1], reverse = True)
# 출력
for d in dap:
    print(d[0]+1)