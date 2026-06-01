def solution(num_list):
    e, o = 0, 0
    for n in num_list:
        if n%2:
            o += 1
        else:
            e += 1
    answer = [e, o]
    return answer