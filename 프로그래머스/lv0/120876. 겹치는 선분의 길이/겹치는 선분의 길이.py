def solution(lines):
    answer = 0
    lst = [0]*200
    for l in lines:
        for i in range(l[0]+100, l[1]+100):
            lst[i] += 1
    for l in lst:
        if l>=2:
            answer += 1
            
    return answer