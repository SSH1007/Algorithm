def solution(d, budget):
    answer = 0
    d.sort()
    for D in d:
        budget -= D
        if budget < 0:
            break
        answer += 1
    return answer