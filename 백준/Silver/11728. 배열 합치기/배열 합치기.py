N, M = map(int, input().split())
Alst = list(map(int, input().split()))
Blst = list(map(int, input().split()))
dap = sorted(Alst+Blst)
print(*dap)