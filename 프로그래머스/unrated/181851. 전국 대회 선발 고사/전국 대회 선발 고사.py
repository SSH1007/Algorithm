def solution(rank, attendance):
    answer = 0
    lst = []
    for i in range(len(rank)):
        lst.append((i, rank[i], attendance[i]))
    lst.sort(key=lambda x:x[1])
    cnt = 0
    dap = []
    for l in lst:
        if l[2]:
            cnt+=1
            dap.append(l[0])
        if cnt == 3:
            break
    answer = dap[0]*10000+dap[1]*100+dap[2]
    return answer