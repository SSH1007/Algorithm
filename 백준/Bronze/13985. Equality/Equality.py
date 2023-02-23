lst = list(input().split())
abc = []
for l in lst:
    if l.isdecimal():
        abc.append(int(l))
if abc[0]+abc[1] == abc[2]:
    print('YES')
else:
    print('NO')