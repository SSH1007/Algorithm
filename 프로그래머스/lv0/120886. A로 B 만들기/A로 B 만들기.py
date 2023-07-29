def solution(before, after):
    answer = 0
    b = list(before)
    a = list(after)
    if sorted(a) == sorted(b):
        answer = 1
    return answer