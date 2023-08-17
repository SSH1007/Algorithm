def solution(n):
    answer = 0
    sosu = [0]*(n+1)
    for i in range(2, int(n**0.5)+1):
        if not sosu[i]:
            for j in range(i+i, n+1, i):
                sosu[j] = 1
    answer = sosu[2:].count(0)
    return answer