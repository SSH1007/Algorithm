def solution(my_string, indices):
    answer = ''
    for m in range(len(my_string)):
        if m not in indices:
            answer += my_string[m]
    return answer