def solution(arr):
    i = 0
    while len(arr) > 2**i:
        i += 1
    answer = arr+[0]*(2**i-len(arr))
    return answer