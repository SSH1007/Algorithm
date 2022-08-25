limit = int(input())
speed = int(input())
over = speed - limit
txt = 'You are speeding and your fine is $'
if over >= 31:
    print(f'{txt}500.')
elif over >= 21:
    print(f'{txt}270.')
elif over >= 1:
    print(f'{txt}100.')
else:
    print('Congratulations, you are within the speed limit!')