import sys
input = sys.stdin.readline
S = input().rstrip()
dap = []
for s in S:
    if s == 'U' or s == 'C' or s == 'P':
        dap.append(s)
cnt = 0
for i in ''.join(dap):
    if i == 'U' and cnt == 0:
        cnt = 1
    elif i == 'C' and cnt == 1:
        cnt = 2
    elif i == 'P' and cnt == 2:
        cnt = 3
    elif i == 'C' and cnt == 3:
        cnt =4
        break
if cnt == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')