def solution(sizes):
    answer = 0
    w, h = 0, 0
    for s in sizes:
        w = max(w, max(s))
        h = max(h, min(s))
    answer = w*h
    return answer