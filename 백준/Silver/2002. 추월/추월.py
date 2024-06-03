import sys
input = sys.stdin.readline
N = int(input().rstrip())
enterCar = [input().rstrip() for _ in range(N)]
exitCar = [input().rstrip() for _ in range(N)]
# 나간 차들의 순서를 딕셔너리에 저장
exitIndex = {car: idx for idx, car in enumerate(exitCar)}
dap = 0
# 현재까지 나간 차들 중 가장 마지막 차의 순번
lastCarIndex = -1

# 들어온 순서대로, 실제 나간 순서와 비교
for car in enterCar:
    # 현재 차량의 실제 나간 순번
    order = exitIndex[car]
    # 현재 차량이 실제로 나간 순번이 이미 나간 차의 수와 같거나 크다면
    if order >= lastCarIndex:
        # 가장 마지막으로 나간 차의 순번을 갱신
        lastCarIndex = order
    # 현재 차량이 실제로 나간 순번이
    # 현재까지 나간 차들 중 가장 마지막 순번보다 작다면(이른 순번이라면?)
    else:
        # 추월당했다는 뜻
        dap += 1
print(dap)