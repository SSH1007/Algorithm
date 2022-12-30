# 전체 문자열 H
H = input()
# 탐색할 문자열 N
N = input()
# 시작점 초기화
start = 0
# N의 등장횟수 초기화
cnt = 0
# 무한 반복
while 1:
    # h는 전체 문자열의 시작점~끝점 범위의 문자열
    h = H[start:]
    # 새로운 시작점은 H에서 N의 첫 위치
    newStart = h.find(N)
    # 만약 newStart가 -1이면(못 찾았으면)
    if newStart==-1:
        # 탈출
        break
    # N의 등장횟수 +=1
    cnt+=1
    # 새로운 시작점에 N의 길이를 더한다
    newStart+=len(N)
    # 전체 문자열 갱신
    H = h
    # 시작점 갱신
    start = newStart
# 등장 횟수 출력
print(cnt)