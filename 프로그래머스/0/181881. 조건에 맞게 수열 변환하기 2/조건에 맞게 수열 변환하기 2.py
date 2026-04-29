def solution(arr):
    answer = 0
    tmp = arr[:]
    while 1:
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2:
                arr[i] *= 2
                arr[i] += 1
        # print(tmp, arr)
        if tmp == arr:
            break
        tmp = arr[:]
        answer += 1
    return answer