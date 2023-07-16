def solution(n):
    answer = 0
    lst = [i for i in range(n+1)]
    
    for i in range(2, n+1):
        if lst[i] == 0:
            continue
        for j in range(2*i, n+1, i):
            lst[j] = 0
    
    for i in range(n+1):
        if i>3 and lst[i] == 0:
            answer += 1
    return answer