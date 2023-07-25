def solution(numbers):
    answer = -100000000
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer = max(answer, numbers[i]*numbers[j])
    return answer