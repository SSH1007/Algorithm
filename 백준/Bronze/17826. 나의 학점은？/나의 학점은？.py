lst = list(map(int, input().split()))
score = int(input())
i = lst.index(score)
if i < 5:
    print('A+')
elif i < 15:
    print('A0')
elif i < 30:
    print('B+')
elif i < 35:
    print('B0')
elif i < 45:
    print('C+')
elif i < 48:
    print('C0')
else:
    print('F')