def solution(num, k):
    answer = 0
    idx = str(num).find(str(k))
    if idx == -1:
        answer = -1
    else:
        answer = idx+1
    return answer