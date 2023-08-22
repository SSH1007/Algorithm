def solution(dartResult):
    answer = 0
    lst = []
    start, end = 0, 0
    while end < len(dartResult):
        a = dartResult[end]
        if a == '*':
            if len(lst)>1:
                lst[-2] = lst[-2]*2
            lst[-1] = lst[-1]*2
            start += 1
        elif a == '#':
            lst[-1] = lst[-1] * -1
            start += 1
        elif a == 'S':
            lst.append(int(dartResult[start:end]))
            start = end+1
        elif a == 'D':
            lst.append(int(dartResult[start:end])**2)
            start = end+1
        elif a == 'T':
            lst.append(int(dartResult[start:end])**3)
            start = end+1
        end += 1
    print(lst)
    answer = sum(lst)
    return answer