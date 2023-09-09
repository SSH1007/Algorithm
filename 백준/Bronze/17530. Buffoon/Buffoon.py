N = int(input())
s = int(input())
flag = True
for _ in range(N-1):
    v = int(input())
    if s < v:
        flag = False
if flag:
    print('S')
else:
    print('N')