def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        answer = True
        for n in range(len(s)):
            if not s[n].isdigit():
                answer = False
                break
    return answer