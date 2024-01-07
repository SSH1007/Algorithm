N = int(input())
# 65, 97
Nlst = list(map(int, input().split()))
a = ''.join(sorted(list(input())))
hint = []
for n in Nlst:
    if n == 0:
        hint.append(' ')
    else:
        if 1<=n<=26:
            hint.append(chr(n+64))
        elif 27<=n<=57:
            hint.append(chr(n+70))
b = ''.join(sorted(hint))
if a == b:
    print('y')
else:
    print('n')