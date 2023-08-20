def solution(N, stages):
    answer = []
    tmp = []
    for n in range(1, N+1):
        a, b = 0, 0
        for s in stages:
            if s >= n:
                b += 1
            if s == n:
                a += 1
        if b == 0:
            tmp.append((n, 0))
        else:
            tmp.append((n, a/b))
    tmp.sort(key = lambda x:(-x[1], x[0]))
    for t in tmp:
        answer.append(t[0])
    return answer