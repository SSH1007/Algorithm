# 테스트 케이스 개수 T
T = int(input())
# 답 리스트 초기화
lst = []
# T번 반복
for _ in range(T):
    # 구분하는 공백 줄 입력
    sep = input()
    # 학생의 수 N 입력
    N = int(input())
    # 사탕의 개수 초기화
    dap = 0
    # 학생이 가진 사탕의 수 입력받아서 더하기
    for _ in range(N):
       dap += int(input())
    # 총합을 균등하게 나눌 수 있으면 YES 추가
    if dap%N==0:
        lst.append('YES')
    # 못하면 NO 추가
    else:
        lst.append('NO')
# YES와 NO 출력
print(*lst, sep = '\n')