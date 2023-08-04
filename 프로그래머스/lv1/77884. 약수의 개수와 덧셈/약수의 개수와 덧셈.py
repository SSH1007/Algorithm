def yark(n):
    dap = 0
    for i in range(1, n+1):
        if n%i == 0:
            dap += 1
    return dap

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if yark(i)%2:
            answer -= i
        else:
            answer += i
    return answer