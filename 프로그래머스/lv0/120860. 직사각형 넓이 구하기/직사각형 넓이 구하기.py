def solution(dots):
    answer = 0
    sx, bx, sy, by = 256, -256, 256, -256
    for x, y in dots:
        sx = min(sx, x)
        sy = min(sy, y)
        bx = max(bx, x)
        by = max(by, y)
    answer = (bx-sx)*(by-sy)
    return answer