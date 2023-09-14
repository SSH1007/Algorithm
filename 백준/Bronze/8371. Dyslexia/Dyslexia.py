N = int(input())
A = input()
B = input()
dap = 0
for n in range(N):
    if A[n] != B[n]:
        dap += 1
print(dap)