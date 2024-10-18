x, y, c = map(float, input().split())
# c는 빗변 x, y의 길이를 넘을 수 없으므로
s, e = 1, min(x, y)
dap = 0.0
# 10^-3까지는 허용한다는건 오차가 10^-3 이내이면 종료한다는 뜻
while e - s > 0.001:
    # mid == z
    mid = (s+e)/2
    a = ((x**2)-(mid**2))**0.5
    b = ((y**2)-(mid**2))**0.5
    C = (a*b)/(a+b)
    # mid값이 작아지면 a,b가 커지고, mid값이 커지면 a,b가 작아진다
    # 따라서 예상값 C가 주어진 값 c보다 크거나 같으면
    # C값을 줄이고 이분탐색을 더 실행하기 위해 mid값을 늘려야 한다.
    # 따라서 s를 mid로
    if C >= c:
        dap = mid
        s = mid
    else:
        e = mid
print(f'{dap:.3f}')