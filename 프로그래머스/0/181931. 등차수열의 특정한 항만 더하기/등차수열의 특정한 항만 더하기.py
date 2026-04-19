def solution(a, d, included):
    answer = 0
    start = a
    for i in range(len(included)):
        if included[i]:
            answer += start
        start += d
    return answer