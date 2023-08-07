def solution(s):
    answer = 0
    dap = ''
    dic = {'zero':'0','one':'1', 'two':'2', 'three':'3','four':'4','five':'5','six':'6','seven':'7', 'eight':'8', 'nine':'9'}
    tmp = ''
    for i in range(len(s)):
        if s[i].isalpha():
            tmp += s[i]
            if tmp in dic:
                dap += dic[tmp]
                tmp = ''
        else:
            dap += str(s[i])
    answer = int(dap)
    return answer