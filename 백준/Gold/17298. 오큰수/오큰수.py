N = int(input())
A = list(map(int, input().split()))
stack = [0]
dap = [-1]*N
# 앞에서 순서대로 dap에 오큰수를 넣는게 아니라, 
# 오큰수를 먼저 구하고 스택의 인덱스에 맞게 다시 넣는 형태
for i in range(1,N):
    while stack and A[stack[-1]] < A[i]:
        dap[stack.pop()] = A[i]
    stack.append(i)
print(*dap)