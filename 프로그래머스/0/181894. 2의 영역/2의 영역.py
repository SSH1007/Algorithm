def solution(arr):
    s, e = 100000, 0
    for i in range(len(arr)):
        if arr[i] == 2:
            s = min(s, i)
            e = max(s, i)
    answer = arr[s:e+1]
    if not answer:
        answer = [-1]
    return answer