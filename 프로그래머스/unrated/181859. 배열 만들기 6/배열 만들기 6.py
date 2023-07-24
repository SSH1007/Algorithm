def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk and stk[-1]==arr[i]:
            stk.pop()
            i += 1
        elif stk and stk[-1]!=arr[i]:
            stk.append(arr[i])
            i += 1
    if not stk:
        stk.append(-1)
    return stk