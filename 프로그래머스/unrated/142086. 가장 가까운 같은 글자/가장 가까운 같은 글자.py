def solution(s):
    answer = []
    alpha = [0]*27
    for n in range(len(s)):
        if alpha[ord(s[n])-96] == 0:
            answer.append(-1)
        else:
            answer.append(n-alpha[ord(s[n])-96]+1)
        alpha[ord(s[n])-96] = n+1
    return answer