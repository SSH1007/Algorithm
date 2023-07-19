def solution(order):
    answer = 0
    lst = [0]*10
    for o in str(order):
        if o!='0' and int(o)%3==0:
            lst[int(o)]+=1
    answer = sum(lst)
    return answer