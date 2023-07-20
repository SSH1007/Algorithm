def solution(myString, pat):
    answer = 0
    s, p = '', pat.upper()
    for m in myString:
        s += m.upper()
    if p in s:
        answer = 1
    return answer