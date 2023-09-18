N, K = map(int, input().split())
dap = []


def f(x):
    return int(str(x)[-1])


for x in range(1, N+1):
    if f(x) != f(K) and f(x) != f(2*K):
        dap.append(x)
print(len(dap))
print(*dap)