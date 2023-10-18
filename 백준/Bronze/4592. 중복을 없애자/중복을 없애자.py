while 1:
    submit = list(map(int, input().split()))
    if submit[0] == 0:
        break
    start = -1
    lst = []
    for s in range(1, submit[0]+1):
        if start != submit[s]:
            lst.append(submit[s])
            start = submit[s]
    print(*lst, '$')