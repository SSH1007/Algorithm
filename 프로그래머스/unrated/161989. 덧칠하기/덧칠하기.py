def solution(n, m, section):
    answer = 1
    start = section[0]
    for s in section:
        if start + m - 1 >= s:
            continue
        answer += 1
        start = s
    
    return answer