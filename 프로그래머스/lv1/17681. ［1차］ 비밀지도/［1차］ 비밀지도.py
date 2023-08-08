def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = bin(arr1[i]|arr2[i])
        row = tmp[2:].zfill(n)
        dap = ''
        for r in row:
            if r == '1':
                dap += '#'
            else:
                dap += ' '
        answer.append(dap)
    return answer