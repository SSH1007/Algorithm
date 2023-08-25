def solution(lottos, win_nums):
    answer = []
    lot = [0]*46
    zero = 0
    for l in lottos:
        if l == 0:
            zero += 1
        else:
            lot[l] += 1
    for w in win_nums:
        lot[w] += 1
    dap = 0
    for i in range(46):
        if lot[i] > 1:
            dap += 1
    lst = [dap+zero, dap]
    for l in lst:
        if l == 6:
            answer.append(1)
        elif l == 5:
            answer.append(2)
        elif l == 4:
            answer.append(3)
        elif l == 3:
            answer.append(4)
        elif l == 2:
            answer.append(5)
        else:
            answer.append(6)
    return answer