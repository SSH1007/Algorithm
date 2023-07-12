def solution(n):
    answer = 0
    lst = []
    for i in range(1, n+1):
        if n%i == 0:
            tmp = []
            tmp.append(i)
            tmp.append(n//i)
            lst.append(tmp)
    print(lst)
    answer = len(lst)
    return answer