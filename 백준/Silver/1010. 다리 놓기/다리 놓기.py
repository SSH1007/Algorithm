# 다리 놓기
# 조합 문제임
# nCr은 n!//(r!*(n-r)!)
# 팩토리얼 함수
def fact(n):
    dap = 1
    for i in range(1,n+1):
        dap*=i
    return dap

# 메인 코드
T = int(input())    # 테스트 케이스 개수 받기
for _ in range(T):  # 받은 케이스 개수만큼 반복문
    # 서쪽과 동쪽 사이트 받기
    r, n = map(int, input().split())
    # 팩토리얼 함수로 조합 계산
    dap = fact(n)//(fact(r)*fact(n-r))
    print(dap)