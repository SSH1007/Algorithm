a, b = map(int, input().split())
c, d = map(int, input().split())
dap = []
dap.append(a/c+b/d)
dap.append(c/d+a/b)
dap.append(d/b+c/a)
dap.append(b/a+d/c)
print(dap.index(max(dap)))