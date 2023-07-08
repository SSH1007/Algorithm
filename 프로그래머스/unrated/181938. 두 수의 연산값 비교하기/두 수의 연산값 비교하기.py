def solution(a, b):
    answer = 0
    aa = int(str(a)+str(b))
    bb = 2*a*b
    if aa >= bb:
        answer = aa
    else:
        answer = bb
    return answer