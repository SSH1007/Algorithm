import sys
input = sys.stdin.readline

W, H, X, Y, P = map(int, input().rstrip().split())
dap = 0
for _ in range(P):
    x, y = map(int, input().rstrip().split())
    # 직사각형 범위
    if X <= x <= X+W and Y <= y <= Y+H:
        dap += 1
    # 좌우의 반원 범위
    elif ((X-x)**2 + (Y+(H//2)-y)**2)**0.5 <= H//2:
        dap += 1
    elif ((X+W-x)**2 + (Y+(H//2)-y)**2)**0.5 <= H//2:
        dap += 1

print(dap)