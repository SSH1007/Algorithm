# 트로피의 개수 N 입력
N = int(input())
# 빈 리스트 생성
trophy = []
# N개 트로피들의 높이 받아서 리스트에 넣기
for _ in range(N):
    trophy.append(int(input()))
# 가장 높은 트로피의 높이 초기화
maxheight = 0
# 왼쪽에서 봤을 때 트로피의 개수 초기화
leftCnt = 0
# 왼쪽에서 가면서 보이는 개수 세기
for n in range(N):
    if trophy[n] > maxheight:
        maxheight = trophy[n]
        leftCnt+=1
# 답 출력
print(leftCnt)
# 가장 높은 트로피의 높이 초기화
maxheight = 0
# 오른쪽에서 봤을 때 트로피의 개수 초기화
rightCnt = 0
# 오른쪽에서 가면서 보이는 개수 세기
for n in range(N-1, -1, -1):
    if trophy[n] > maxheight:
        maxheight = trophy[n]
        rightCnt+=1
# 답 출력
print(rightCnt)