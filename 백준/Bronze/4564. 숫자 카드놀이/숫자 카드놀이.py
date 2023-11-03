while 1:
    S = int(input())
    if S == 0:
        break
    print(S, end=' ')
    lst = []
    while S%10 != S:
        tmp = 1
        for s in str(S):
            tmp *= int(s)
        lst.append(tmp)
        S = tmp
    print(*lst)