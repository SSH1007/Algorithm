def solution(n):
    answer = []
    d = 2

    while d <= n:
        if n % d == 0:
            answer.append(d)
            n = n / d
        else:
            d = d + 1
            
    answer = list(set(answer))
    answer.sort()
    return answer