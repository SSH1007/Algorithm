def solution(rny_string):
    answer = ''
    for r in rny_string:
        if r == 'm':
            answer += 'rn'
        else:
            answer += r
    return answer