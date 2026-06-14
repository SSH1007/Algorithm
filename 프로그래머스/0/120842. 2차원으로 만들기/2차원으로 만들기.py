def solution(num_list, n):
    answer = []
    for i in range(len(num_list)//n):
        tmp = []
        for j in range(i*n, i*n+n):
            tmp.append(num_list[j])
        answer.append(tmp)            
    return answer