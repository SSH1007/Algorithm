def solution(cipher, code):
    answer = ''
    for c in range(code, len(cipher)+1, code):
        answer += cipher[c-1]
    return answer