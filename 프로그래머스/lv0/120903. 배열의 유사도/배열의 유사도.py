def solution(s1, s2):
    answer = 0
    for s in s1:
        for ss in s2:
            if s == ss:
                answer += 1
                break
    return answer