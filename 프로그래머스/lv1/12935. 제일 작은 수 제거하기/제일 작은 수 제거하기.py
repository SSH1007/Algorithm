def solution(arr):
    answer = []
    m = min(arr)
    for a in arr:
        if a != m:
            answer.append(a)
    if not answer:
        answer = [-1]
    return answer