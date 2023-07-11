def solution(n):
    answer = [n]
    while n!=1:
        if n%2:
            n = 3*n+1
            answer.append(n)
        else:
            n //= 2
            answer.append(n)
    return answer