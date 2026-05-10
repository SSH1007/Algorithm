def solution(arr):
    answer = []
    if len(arr) < len(arr[0]):
        for a in arr:
            answer.append(a)
        for _ in range(len(arr[0])-len(arr)):
            answer.append([0]*len(arr[0]))
    else:
        for a in arr:
            answer.append(a+[0]*(len(arr)-len(arr[0])))
    return answer