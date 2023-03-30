C, K, P = map(int, input().split())
dap = 0
for c in range(1, C+1):
    dap+=K*c+P*(c**2)
print(dap)