def solution(n_str):
    answer = ''
    flag = 0
    for n in n_str:
        if n != '0':
            flag = 1
        if flag:
            answer += n
    return answer