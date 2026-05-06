def solution(rank, attendance):
    answer = 0
    lst = []
    for i in range(len(rank)):
        if attendance[i]:
            lst.append((i, rank[i]))
    lst.sort(key=lambda x:x[1])
    answer = lst[0][0]*10000 + lst[1][0]*100 + lst[2][0]
    return answer