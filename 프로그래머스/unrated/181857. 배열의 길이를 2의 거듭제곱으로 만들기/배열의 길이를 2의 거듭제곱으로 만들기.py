def solution(arr):
    answer = []
    i = 0
    while 1:
        if 2**i >= len(arr):
            break
        i += 1
    for _ in range(len(arr), 2**i):
        arr.append(0)
    answer = arr
    return answer