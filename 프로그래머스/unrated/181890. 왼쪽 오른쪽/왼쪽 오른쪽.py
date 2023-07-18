def solution(str_list):
    answer = []
    for s in range(len(str_list)):
        if str_list[s] == 'l':
            answer = str_list[:s]
            break
        elif str_list[s] == 'r':
            answer = str_list[s+1:]
            break
    return answer