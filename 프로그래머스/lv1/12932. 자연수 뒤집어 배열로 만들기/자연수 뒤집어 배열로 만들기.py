def solution(n):
    answer = []
    N = len(str(n))
    for s in range(N-1, -1, -1):
        answer.append(int(str(n)[s]))
    return answer