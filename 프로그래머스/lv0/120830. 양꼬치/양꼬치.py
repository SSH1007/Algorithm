def solution(n, k):
    answer = 0
    answer += 12000 * n
    nk = max(k-n//10, 0)
    answer += 2000*nk
    return answer