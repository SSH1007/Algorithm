import copy

def solution(arr):
    answer = 0
    start = copy.deepcopy(arr)
    lst = [start]
    while 1:
        for n in range(len(arr)):
            if arr[n]>=50 and arr[n]%2==0:
                arr[n]//=2
            elif arr[n]<50 and arr[n]%2:
                arr[n]*=2
                arr[n]+=1
        tmp = copy.deepcopy(arr)
        lst.append(tmp)
        if lst[-1] == lst[-2]:
            break
        answer += 1
        
    return answer