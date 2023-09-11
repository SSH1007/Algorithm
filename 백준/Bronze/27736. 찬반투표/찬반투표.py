N = int(input())
vote = list(map(int, input().split()))
agree = 0
disagree = 0
retire = 0
for v in vote:
    if v == 1:
        agree += 1
    elif v == -1:
        disagree += 1
    else:
        retire += 1
if retire >= N/2:
    print('INVALID')
elif agree > disagree:
    print('APPROVED')
else:
    print('REJECTED')