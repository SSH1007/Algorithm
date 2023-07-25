def solution(my_string):
    answer = 0
    lst = []
    idx = 0
    while idx < len(my_string):
        tmp = []
        if my_string[idx].isdigit():
            tmp.append(my_string[idx])
            for i in range(idx + 1, len(my_string)):
                if not my_string[i].isdigit():
                    idx += (i - idx)
                    break
                tmp.append(my_string[i])
                idx += 1
            lst.append(''.join(tmp))
        idx += 1

    for l in lst:
        answer += int(l)

    return answer