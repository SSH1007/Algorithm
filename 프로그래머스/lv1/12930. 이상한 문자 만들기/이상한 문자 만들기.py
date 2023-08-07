def solution(s):
    answer = ''
    idx = 0
    for n in range(len(s)):
        if idx%2:
            answer += s[n].lower()
        else:
            answer += s[n].upper()
        if s[n] == ' ':
            idx = 0
        else:
            idx+=1
        
    return answer