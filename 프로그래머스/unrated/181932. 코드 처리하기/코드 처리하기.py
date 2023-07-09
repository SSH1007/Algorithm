def solution(code):
    answer = ''
    mode = 0
    for idx in range(len(code)):
        if mode == 0:
            if code[idx]!='1':
                if idx%2 == 0:
                    answer += code[idx]
            else:
                mode = abs(mode-1)
        elif mode == 1:
            if code[idx]!='1':
                if idx%2:
                    answer += code[idx]
            else:
                mode = abs(mode-1)
    if answer == '':
        answer = 'EMPTY'
    return answer