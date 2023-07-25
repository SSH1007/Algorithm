S = input()
S = S.replace('pi', ' ')
S = S.replace('ka', ' ')
S = S.replace('chu', ' ')
S = S.replace(' ', '')
if len(S) == 0:
    print('YES')
else:
    print('NO')