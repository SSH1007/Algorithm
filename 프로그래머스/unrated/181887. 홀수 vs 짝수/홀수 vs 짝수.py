def solution(num_list):
    answer = 0
    odd, even = 0, 0
    for n in range(len(num_list)):
        if n%2:
            odd += num_list[n]
        else:
            even += num_list[n]
    answer = max(odd, even)
    return answer