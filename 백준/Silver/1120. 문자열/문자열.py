A, B = input().split()
# A,B의 길이는 최대 50
dap = 50
# 긴걸 기준으로 작은걸 왔다갔다하면서 최솟값 찾기
for i in range(len(B)-len(A)+1):
    tmp = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            tmp += 1
    dap = min(dap, tmp)
print(dap)