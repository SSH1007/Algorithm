def solution(balls, share):
    answer = 0
    mom, son = 1, 1
    for b in range(balls, share, -1):
        mom *= b
    for ms in range(1, balls-share+1):
        son *= ms
    answer = mom//son
    
    return answer