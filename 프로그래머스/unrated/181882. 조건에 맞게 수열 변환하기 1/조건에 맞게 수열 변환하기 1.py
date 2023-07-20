def solution(arr):
    answer = []
    for n in range(len(arr)):
        if arr[n] >= 50 and arr[n]%2==0:
            arr[n]//=2
        elif arr[n] < 50 and arr[n]%2:
            arr[n]*=2
    answer = arr
    return answer