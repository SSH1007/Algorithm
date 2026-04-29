def F(n):
    c = 0
    while 1:
        if n == 1:
            break
        if n%2:
            n-=1
            n//=2
        else:
            n//=2
        c+=1
    return c

def solution(num_list):
    answer = 0
    for n in num_list:
        answer += F(n)
    return answer