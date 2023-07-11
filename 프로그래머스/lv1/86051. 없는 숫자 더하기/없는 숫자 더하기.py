def solution(numbers):
    answer = 0
    lst = [0]*10
    for n in numbers:
        lst[n] += 1
    for i in range(10):
        if lst[i] == 0:
            answer += i
        
    return answer