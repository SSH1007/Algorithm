def solution(myString, pat):
    answer = ''
    idx = 0
    for i in range(len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            idx = i
    answer = myString[:idx+len(pat)]
    return answer