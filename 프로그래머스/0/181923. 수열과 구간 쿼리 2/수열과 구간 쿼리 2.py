def solution(arr, queries):
    answer = []
    for q in queries:
        s, e, k = q[0], q[1], q[2]
        tmp = 1000000
        for i in range(s, e+1):
            if arr[i] > k:
                tmp = min(tmp, arr[i])
        if tmp == 1000000:
            tmp = -1
        answer.append(tmp)
    return answer