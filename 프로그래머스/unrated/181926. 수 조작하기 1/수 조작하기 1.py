def solution(n, control):
    answer = 0
    for c in control:
        if c == 'w':
            n+=1
        elif c == 's':
            n-=1
        elif c == 'd':
            n+=10
        elif c == 'a':
            n-=10
    answer = n
    return answer