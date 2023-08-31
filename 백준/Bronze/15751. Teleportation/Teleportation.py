a, b, x, y = map(int, input().split())
dap1 = abs(a-x) + abs(b-y)
dap2 = abs(a-y) + abs(b-x)
print(min(dap1, dap2, abs(b-a)))