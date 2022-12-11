# 세븐 25의 삼각김밥 가격 정보 : Y그램당 X원
X, Y = map(int, input().split())
# 세븐 25의 삼각김밥 1000그램의 가격
dap = 1000*X/Y
# 세븐25를 제외한 편의점의 개수 N
N = int(input())
# N번 반복하면서 다른 편의점의 삼각김밥의 정보를 받는다
for _ in range(N):
    xi, yi = map(int, input().split())
    # 다른 편의점의 삼각김밥 1000그램이 세븐 25의 가격보다 싸다면
    if 1000*xi/yi < dap:
        # 최저가를 갱신한다
        dap = 1000*xi/yi
# 소수점 2자리까지의 답을 출력한다
print(round(dap,2))