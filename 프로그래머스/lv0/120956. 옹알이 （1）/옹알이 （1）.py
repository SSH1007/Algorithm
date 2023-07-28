def solution(babbling):
    answer = 0
    lst = []
    for b in babbling:
        for i in ['aya', 'ye', 'woo', 'ma']:
            b = b.replace(i, '*')
        lst.append(b)

    for l in lst:
        for i in range(len(l)):
            if l[i]!='*':
                break
        else:
            answer += 1    
    return answer