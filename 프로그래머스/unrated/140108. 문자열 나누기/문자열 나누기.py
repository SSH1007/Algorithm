def solution(s):
    answer = 0
    lst = []
    while len(s) > 0:
        x = s[0]
        xCnt, oCnt = 0, 0
        for i in range(len(s)):
            if s[i] == x:
                xCnt += 1
            else:
                oCnt += 1
            if xCnt == oCnt:
                break
        lst.append(s[:i+1])
        s = s[i+1:]
    answer = len(lst)  
    return answer