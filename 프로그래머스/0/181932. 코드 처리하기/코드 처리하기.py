def solution(code):
    mode = 0
    answer = ''
    for idx in range(len(code)):
        if mode:
            if code[idx] != '1':
                if idx%2:
                    answer += code[idx]
            else:
                mode = 0
        else:
            if code[idx] != '1':
                if idx%2 == 0:
                    answer += code[idx]
            else:
                mode = 1
    if answer == '':
        return 'EMPTY'
    return answer