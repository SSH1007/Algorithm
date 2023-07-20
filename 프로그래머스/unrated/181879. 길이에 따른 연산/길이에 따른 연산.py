def solution(num_list):
    answer = 0
    if len(num_list) > 10:
        answer = sum(num_list)
    else:
        answer = 1
        for n in num_list:
            answer *= n
    return answer