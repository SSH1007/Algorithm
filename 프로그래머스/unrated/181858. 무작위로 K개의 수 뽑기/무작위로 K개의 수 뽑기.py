def solution(arr, k):
    answer = []
    for a in arr:
        if a not in answer:
            answer.append(a)
    while len(answer) > k:
        answer.pop()
    while len(answer) < k:
        answer.append(-1)
    return answer