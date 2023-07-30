def solution(arr):
    answer = [[]]
    r = len(arr)
    c = len(arr[0])
    # print(r, c)
    if r > c:
        for a in arr:
            for _ in range(r-c):
                a.append(0)
    else:
        for _ in range(c-r):
            arr.append([0]*c)
    answer = arr
    return answer