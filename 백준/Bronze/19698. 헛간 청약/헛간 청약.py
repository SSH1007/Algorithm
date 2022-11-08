N, W, H, L = map(int, input().split())
dap = (W//L) * (H//L)
print(dap if dap<=N else N)