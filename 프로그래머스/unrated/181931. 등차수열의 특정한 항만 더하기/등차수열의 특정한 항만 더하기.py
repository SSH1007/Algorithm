def solution(a, d, included):
    print(included)
    answer = 0
    idx = 0
    while idx<len(included):
        if included[idx]:
            answer += a
        a+=d
        idx+=1
    return answer