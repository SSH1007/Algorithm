def solution(myStr):
    myStr+='a'
    answer = []
    tmp = ''
    for m in myStr:
        if m == 'a' or m == 'b' or m == 'c':
            if len(tmp) > 0:
                answer.append(tmp)
                tmp = ''
        else:
            tmp += m    
    if not answer:
        answer.append('EMPTY')
    return answer