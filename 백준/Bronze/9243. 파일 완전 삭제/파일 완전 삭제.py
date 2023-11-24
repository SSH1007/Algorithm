N = int(input())
S = input()
E = input()
D = ''
for s in S:
    if N%2:
        if s == '1':
            D += '0'
        else:
            D += '1'
    else:
        D += s
if D != E:
    print('Deletion failed')
else:
    print('Deletion succeeded')