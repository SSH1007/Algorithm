dic = {46:46, 79:79, 45:124, 124:45, 47:92, 92:47, 94:60, 60:118, 118:62, 62:94}

N, M = map(int, input().split())
dap = [[] for _ in range(M)]
for _ in range(N):
    S = input()
    for i in range(M):
        dap[i].append(chr(dic[ord(S[i])]))
for d in dap[::-1]:
    print(*d, sep='')