# 1475번 : 방 번호
# 각 숫자의 등장빈도를 기록할 리스트 초기화
lst = [0]*10
# 방 번호 N 입력
N = input()
# N을 순회하면서
for i in range(len(N)):
    # 6이나 9라면
    if N[i] in ['6','9']:
        # 6과 9를 혼용할 수 있으므로, 가능한 한 한 세트로 세도록 계산
        if lst[6] <= lst[9]:
            lst[6]+=1
        else:
            lst[9]+=1
    # 나머지의 경우는 단순히 1 증가
    else:
        lst[int(N[i])]+=1
# 리스트 안의 최대값 출력
print(max(lst))