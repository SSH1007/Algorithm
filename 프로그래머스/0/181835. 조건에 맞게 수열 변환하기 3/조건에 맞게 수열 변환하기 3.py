def solution(arr, k):
    answer = []
    for a in arr:
        if k%2:
            answer.append(a*k)
        else:
            answer.append(a+k)
    return answer