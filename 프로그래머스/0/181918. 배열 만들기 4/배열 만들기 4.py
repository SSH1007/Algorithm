def solution(arr):
    stk = []
    i = 0
    while 1:
        if i >= len(arr):
            break
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()
    return stk