def solution(num_list):
    answer = -1
    for n in range(len(num_list)):
        if num_list[n] < 0:
            answer = n
            break
    return answer