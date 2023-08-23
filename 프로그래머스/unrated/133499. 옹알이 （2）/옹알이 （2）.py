def solution(babbling):
    answer = 0
    lst = ['aya', 'ye', 'woo', 'ma']
    for i in range(len(babbling)):
        for l in lst:
            if l in babbling[i] and l*2 not in babbling[i]:
                babbling[i] = babbling[i].replace(l, '*')
        for j in babbling[i]:
            if j != '*':
                break
        else:
             answer += 1   
        
    return answer