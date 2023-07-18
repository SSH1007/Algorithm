def solution(s):
    answer = 0
    lst = list(s.split())
    print(lst)
    for l in range(len(lst)):
        if lst[l] == 'Z':
            answer -= int(lst[l-1])
        else:
            answer += int(lst[l])
    return answer