def solution(s):
    answer = ''
    flag = True
    for n in range(len(s)):
        if s[n] == ' ':
            flag = True
            answer += ' '
        else:
            if flag:
                answer += s[n].upper()
                flag = False
            else:
                answer += s[n].lower()
    return answer