def solution(num_list):
    a, b = 0, 0
    a_cnt, b_cnt = 1, 1
    for i in range(len(num_list)-1, -1, -1):
        if num_list[i]%2:
            a += num_list[i]*a_cnt
            a_cnt*=10
        else:
            b += num_list[i]*b_cnt
            b_cnt*=10
    answer = a+b
    return answer