# 박스의 개수 N, 책의 개수 M
N, M = map(int, input().split())
# 박스의 용량 A1...An 입력
Alst = list(map(int, input().split()))
# 책의 크기 B1...Bn 입력
Blst = list(map(int, input().split()))
# 책의 크기들로 순회
for b in range(len(Blst)):
    # 현재 낭비 용량 초기화
    currentWastedBox = 0
    # 1번 박스부터 책을 넣을 수 있는지 순회
    for a in range(len(Alst)):
        # 넣을 수 있으면
        if Blst[b]<=Alst[a]:
            # a번 박스의 용량을 b번 책의 크기만큼 뺀다.
            Alst[a]-=Blst[b]
            # 다음 책으로 넘어가기 위해 박스 순회에서 탈출
            break
# 남은 박스 용량들의 합을 출력
print(sum(Alst))