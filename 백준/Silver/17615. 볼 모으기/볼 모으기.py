def f():
    _ = int(input().rstrip())   # 1 <= N <= 500,000
    balls = input()
    # 빨간색을 움직여 빨간색을 왼쪽으로
    r_R = balls.lstrip('R').count('R')
    # 빨간색을 움직여 빨간색을 오른쪽으로
    R_r = balls.rstrip('R').count('R')
    # 파란색을 움직여 파란색을 왼쪽으로
    b_R = balls.lstrip('B').count('B')
    # 파란색을 움직여 파란색을 오른쪽으로
    R_b = balls.rstrip('B').count('B')
    print(min(r_R, R_r, b_R, R_b))
    return


f()