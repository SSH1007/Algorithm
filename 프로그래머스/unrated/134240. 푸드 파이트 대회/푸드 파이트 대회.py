def solution(food):
    answer = ''
    for n in range(1,len(food)):
        answer += str(n)*(food[n]//2)
    tmp = answer[::-1]
    answer = answer + '0' + tmp
    return answer