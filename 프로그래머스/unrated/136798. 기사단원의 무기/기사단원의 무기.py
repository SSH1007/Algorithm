def solution(number, limit, power):
    answer = 0
    yak = []
    for n in range(1, number+1):
        tmp = []
        for i in range(1, int(n**0.5)+1):
            if n%i == 0:
                tmp.append(i)
                tmp.append(n//i)
        a = len(set(tmp))
        yak.append(a)
    # print(yak)
    for y in yak:
        if y > limit:
            answer += power
        else:
            answer += y
    return answer