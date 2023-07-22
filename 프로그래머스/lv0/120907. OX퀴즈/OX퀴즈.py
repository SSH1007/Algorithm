def solution(quiz):
    answer = []
    for q in quiz:
        a, b, c, d, e = q.split()
        if b == '+':
            if int(a)+int(c) == int(e):
                answer.append("O")
            else:
                answer.append("X")
        elif b == '-':
            if int(a)-int(c) == int(e):
                answer.append("O")
            else:
                answer.append("X")
    return answer