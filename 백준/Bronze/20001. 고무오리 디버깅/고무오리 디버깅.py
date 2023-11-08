p = 0
while 1:
    S = input()
    if S == '고무오리 디버깅 끝':
        break
    if S == '문제':
        p += 1
    elif S == '고무오리':
        if p:
            p -= 1
        else:
            p += 2
if p:
    print('힝구')
else:
    print('고무오리야 사랑해')