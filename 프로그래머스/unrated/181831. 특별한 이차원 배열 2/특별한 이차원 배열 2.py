def solution(arr):
    answer = 1
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                answer = 0
                return answer
    return answer