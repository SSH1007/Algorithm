def solution(n):
    answer = 0
    fact = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    for f in range(len(fact)-1, -1, -1):
        if n >= fact[f]:
            answer = f
            break
    return answer