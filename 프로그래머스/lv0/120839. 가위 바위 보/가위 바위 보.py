def solution(rsp):
    answer = ''
    for l in rsp:
        if l == '2':
            answer += '0'
        elif l == '0':
            answer += '5'
        elif l == '5':
            answer += '2'
    return answer