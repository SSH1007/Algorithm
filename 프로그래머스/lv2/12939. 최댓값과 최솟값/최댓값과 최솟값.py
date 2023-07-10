def solution(s):
    lst = list(map(int, s.split()))
    lst.sort()
    answer = str(lst[0]) + ' ' + str(lst[-1])
    return answer