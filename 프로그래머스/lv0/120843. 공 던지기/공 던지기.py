def solution(numbers, k):
    answer = 0
    idx = (2*(k-1))%len(numbers)
    answer = numbers[idx]
    return answer