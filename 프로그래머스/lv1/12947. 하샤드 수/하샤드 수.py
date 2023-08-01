def solution(x):
    answer = False
    xx = str(x)
    xs = sum(map(int, xx))
    if x%xs==0:
        answer = True
    return answer