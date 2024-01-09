N = int(input())
perm = list(map(int, input().split()))
for i in range(N-1, 0, -1):
    if perm[i-1] > perm[i]:
        for j in range(N-1, i-1, -1):
            if perm[j] < perm[i-1]:
                perm[i-1], perm[j] = perm[j], perm[i-1]
                dap = perm[:i]+sorted(perm[i:], reverse=True)
                print(*dap)
                exit(0)
print(-1)