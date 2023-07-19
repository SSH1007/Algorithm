def solution(array, n):
    answer = 1000
    array.sort(reverse=True)
    for a in array:
        if abs(n-answer) >= abs(n-a):
            answer = a
    return answer