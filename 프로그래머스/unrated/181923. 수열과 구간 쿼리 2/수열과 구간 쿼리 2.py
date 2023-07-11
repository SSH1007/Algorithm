def solution(arr, queries):
    answer = []
    for q in queries:
        tmp = 1000000
        print(q)
        for i in range(q[0], q[1]+1):
            if arr[i] < tmp and arr[i]>q[2]:
                tmp = arr[i]
        if tmp == 1000000:
            tmp = -1
        answer.append(tmp)
        
    return answer