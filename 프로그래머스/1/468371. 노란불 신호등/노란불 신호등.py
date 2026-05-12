def GCD(a, b):
    while b:
        a, b = b, a%b
    return a


def solution(signals):    
    answer = 0
    lights = []
    cycles = []
    for g, y, r in signals:
        lights.append((g, y, r))
        cycles.append(g+y+r)
    tmp = 1
    for c in cycles:
        tmp = GCD(tmp, c)*tmp*c
    for t in range(tmp):
        flag = True
        for g, y, r in lights:
            now = t%(g+y+r)
            if not (g <= now < g+y):
                flag = False
                break
        if flag:
            answer = t+1
            return answer
    else:
        answer = -1
    return answer