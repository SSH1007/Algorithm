def solution(str_list, ex):
    answer = ''
    for s in str_list:
        if not ex in s:
            answer += s
    return answer