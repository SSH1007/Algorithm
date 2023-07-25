def solution(polynomial):
    answer = ''
    lst = list(polynomial.split())

    # 일차항이랑 상수항 구분
    il, sang = [], []
    for l in lst:
        if 'x' in l:
            il.append(l)
        elif l.isdigit():
            sang.append(l)

    # 각각 더하기
    a, b = 0, 0
    for i in il:
        if len(i) == 1:
            a += 1
        else:
            a += int(i[:-1])
    for s in sang:
        b += int(s)
    if b:
        if a == 1:
            answer = 'x + ' + str(b)
        elif a == 0:
            answer = str(b)
        else:
            answer = str(a) + 'x + ' + str(b)
    else:
        if a == 1:
            answer = 'x'
        else:
            if a == 0:
                answer = '0'
            else:
                answer = str(a) + 'x'
    return answer