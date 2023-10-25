x, y = map(int, input().split())
l, s = max(x, y), min(x, y)
a = l/3 if l/3 <= s else s
b = s/2
dap = max(a, b)
print(dap)