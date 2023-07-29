def solution(picture, k):
    answer = []
    for pic in picture:
        tmp = ''
        for p in pic:
            tmp+=p*k
        for _ in range(k):
            answer.append(tmp)
    return answer