def solution(n, lost, reserve):
    answer = 0
    student = [0]*(n+1)
    for i in range(1, n+1):
        if i in reserve:
            student[i] = 2
        if i in lost:
            if student[i]:
                student[i] -= 1
            else:
                student[i] = 0
        if i not in reserve and i not in lost:
            student[i] += 1
    print(student)
    for i in range(1, n+1):
        if student[i] > 1:
            if i-1 > 0 and not student[i-1]:
                student[i] -= 1
                student[i-1] += 1
            elif i+1 < n+1 and not student[i+1]:
                student[i] -= 1
                student[i+1] += 1
    for s in student:
        if s:
            answer += 1
    print(student)
    return answer