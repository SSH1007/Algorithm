def solution(arr, idx):
    answer = -1
    for i in range(len(arr)):
        if i>idx-1 and arr[i]==1:
            answer = i
            break
    return answer