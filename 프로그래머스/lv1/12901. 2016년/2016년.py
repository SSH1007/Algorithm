def solution(a, b):
    dic = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    answer = ''
    month_d = 0
    for i in range(1,a):
        month_d += dic[i]
    day_d = b-1
    print(month_d, day_d)
    dap = (month_d+day_d)%7
    if dap == 0:
        answer = 'FRI'
    elif dap == 1:
        answer = 'SAT'
    elif dap == 2:
        answer = 'SUN'
    elif dap == 3:
        answer = 'MON'
    elif dap == 4:
        answer = 'TUE'
    elif dap == 5:
        answer = 'WED'
    elif dap == 6:
        answer = 'THU'
    return answer