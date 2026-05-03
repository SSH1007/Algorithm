def solution(arr, k):
    answer = []
    for a in arr:
        if a not in answer:
            answer.append(a)
    lst = answer[:k]
    for _ in range(k-len(lst)):
        lst.append(-1)
    return lst