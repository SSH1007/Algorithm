def solution(x1, x2, x3, x4):
    answer = False
    A, B = False, False
    if x1 or x2:
        A = True
    if x3 or x4:
        B = True
    if A and B:
        answer = True
    return answer