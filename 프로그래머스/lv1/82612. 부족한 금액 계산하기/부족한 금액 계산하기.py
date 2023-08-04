def solution(price, money, count):
    answer = 0
    for c in range(1, count+1):
        money-=price*c
    if money<0:
        answer = abs(money)
    return answer