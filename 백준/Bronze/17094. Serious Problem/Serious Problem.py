n = int(input())
s = input()
e, t = 0, 0
for i in s:
    if i == 'e':
        e += 1
    elif i == '2':
        t += 1
if e > t:
    print('e')
elif e < t:
    print(2)
else:
    print('yee')