def solution(my_string):
    answer = ''
    lst = []
    for m in my_string:
        lst.append(m.lower())
    dap = sorted(lst)
    answer = ''.join(dap)
    return answer