def solution(arr, queries):
    answer = []
    for q in queries:
        for i in range(q[0],q[1]+1):
            arr[i] += 1
    answer = arr
    return answer