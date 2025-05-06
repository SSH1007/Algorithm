x, y = map(int, input().split())
dap = 0
dir = 1
move = 1
cur = x
while 1:
    next = x + dir * move
    if (x <= y <= next) or (next <= y <= x):
        dap += abs(y - cur)
        break
    else:
        dap += abs(next - cur)
        cur = next
        move *= 2
        dir *= -1
print(dap)