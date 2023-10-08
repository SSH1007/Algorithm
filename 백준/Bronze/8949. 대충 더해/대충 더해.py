dap = ''
A, B = input().split()
l = max(len(A), len(B))
A = A.zfill(l)
B = B.zfill(l)
for i in range(l):
    dap += str(int(A[i])+int(B[i]))
print(dap)