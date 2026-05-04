def solution(arr, n):
    answer = []
    if len(arr)%2:
        for i in range(len(arr)):
            if i%2 == 0:
                arr[i]+=n
            answer.append(arr[i])
    else:
        for i in range(len(arr)):
            if i%2:
                arr[i]+=n
            answer.append(arr[i])
    return answer