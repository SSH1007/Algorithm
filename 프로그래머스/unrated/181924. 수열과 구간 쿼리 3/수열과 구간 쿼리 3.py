def solution(arr, queries):
    answer = []
    for q in queries:
        arr[q[0]], arr[q[1]] = arr[q[1]], arr[q[0]]
    answer = arr
    return answer