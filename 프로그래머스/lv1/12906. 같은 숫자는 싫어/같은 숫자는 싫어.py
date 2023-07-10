def solution(arr):
    answer = []
    tmp = arr[0]
    answer.append(tmp)
    for i in range(1, len(arr)):
        if tmp != arr[i]:
            answer.append(arr[i])
            tmp = arr[i]
    return answer