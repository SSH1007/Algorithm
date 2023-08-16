def solution(answers):
    answer = []
    A, B, C = 0, 0, 0
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    for n in range(len(answers)):
        if answers[n] == a[n%len(a)]:
            A+=1
        if answers[n] == b[n%len(b)]:
            B+=1
        if answers[n] == c[n%len(c)]:
            C+=1
    dap = [(A,1),(B,2),(C,3)]
    dap.sort()
    if dap[0][0]==dap[2][0]:
        answer = [dap[0][1], dap[1][1], dap[2][1]]
    elif dap[1][0] == dap[2][0]:
        answer = [dap[1][1], dap[2][1]]
    else:
        answer = [dap[2][1]]
    return answer