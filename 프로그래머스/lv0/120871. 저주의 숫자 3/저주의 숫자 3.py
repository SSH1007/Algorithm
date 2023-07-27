def solution(n):
    answer = 0
    lst = [0]*1001
    for i in range(3, 1000, 3):
        lst[i] = 1
    for i in range(1000):
        if '3' in str(i):
            lst[i] = 1
    cnt = 0
    for i in range(1,1000):
        if not lst[i]:
            cnt+=1
        if cnt == n:
            answer = i
            break
    return answer