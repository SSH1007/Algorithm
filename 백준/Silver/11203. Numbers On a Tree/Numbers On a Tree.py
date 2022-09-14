info = list(input().split())
H = int(info[0])
top = 2**(H+1)
cnt = 1
if len(info)>1:
    for d in info[1]:
        if d == 'L':
            cnt*=2
        elif d == 'R':
            cnt = cnt*2+1
print(top-cnt)