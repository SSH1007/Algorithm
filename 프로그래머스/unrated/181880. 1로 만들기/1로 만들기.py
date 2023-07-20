def solution(num_list):
    answer = 0
    for n in num_list:
        while n>1:
            if n%2:
                n = (n-1)//2
            else:
                n //= 2
            answer += 1
    return answer