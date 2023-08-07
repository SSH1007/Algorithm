def solution(s, n):
    answer = ''
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small = 'abcdefghijklmnopqrstuvwxyz' 
    for ss in s:
        if ss == ' ':
            answer += ' '
        else:
            if ss in big:
                answer += big[(big.index(ss)+n)%26]
            elif ss in small:
                answer += small[(small.index(ss)+n)%26]
            
    return answer