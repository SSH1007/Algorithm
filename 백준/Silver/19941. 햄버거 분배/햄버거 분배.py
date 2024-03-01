N, K = map(int, input().split())
table = list(input())
dap = 0
for i in range(N):
    if table[i] == 'H':
        for j in range(max(0, i-K), min(i+K+1, N)):
            if table[j] == 'P':
                table[j] = 'T'
                dap += 1
                break

print(dap)