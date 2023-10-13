N, M, K = map(int, input().split())
while K < 0:
    K += N
dap = (((K-3) % N)+M)
if dap > N:
    dap %= N
print(dap)