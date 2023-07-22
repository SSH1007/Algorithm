def solution(myString, pat):
    answer = 0
    s = myString.find(pat)
    e = s+len(pat)
    if s != -1:
        while s < len(myString):
            if myString[s:e] == pat:
                answer += 1

            s += 1
            e += 1
            
    return answer