def solution(A, B):
    answer = -1
    for n in range(len(A)):
        if A == B:
            answer = n
            break
        A = A[-1]+A[:-1]
    return answer