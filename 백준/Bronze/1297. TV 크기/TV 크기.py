# 대각선 D, 높이 비율 H, 너비 비율 W
D, H, W = map(int, input().split())

x = ((D**2)/(H**2+W**2))**0.5
print(int(x*H), int(x*W))