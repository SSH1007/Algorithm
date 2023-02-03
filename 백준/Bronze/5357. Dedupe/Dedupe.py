N = int(input())
for _ in range(N):
    S = input()
    lst = [S[0]]
    for i in range(1,len(S)):
        if S[i]!=S[i-1]:
            lst.append(S[i])
    print(*lst,sep='')