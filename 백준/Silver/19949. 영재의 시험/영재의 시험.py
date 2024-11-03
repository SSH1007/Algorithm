tmp = []
dap = 0
answer = list(map(int, input().split()))


def Back(depth, score):
    global dap
    if depth == 10:
        if score >= 5:
            dap += 1
        return
    for i in range(1, 6):
        if len(tmp) > 1 and tmp[-2] == tmp[-1] == i:
            continue
        tmp.append(i)
        if answer[len(tmp)-1] == i:
            Back(depth + 1, score+1)
        else:
            if len(tmp) - score > 5:
                tmp.pop()
                continue
            Back(depth + 1, score)
        tmp.pop()


Back(0, 0)
print(dap)