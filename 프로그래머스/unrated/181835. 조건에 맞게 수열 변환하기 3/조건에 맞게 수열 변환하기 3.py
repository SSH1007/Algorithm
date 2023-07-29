def solution(arr, k):
    answer = []
    if k%2:
        answer = [a*k for a in arr]
    else:
        answer = [a+k for a in arr]
    return answer