def solution(arr, query):
    for i in range(len(query)):
        if i%2:
            arr = arr[query[i]:]
        else:
            arr = arr[:query[i]+1]
    answer = arr
    return answer