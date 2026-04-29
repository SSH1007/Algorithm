def solution(arr):
    answer = []
    for a in arr:
        if a >= 50 and a % 2 == 0:
            answer.append(a//2)
        elif a < 50 and a % 2:
            answer.append(a*2)
        else:
            answer.append(a)
    return answer