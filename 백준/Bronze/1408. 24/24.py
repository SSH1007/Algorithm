ct = list(map(int,input().split(':')))
st = list(map(int,input().split(':')))
t = (st[0]*3600 + st[1]*60 + st[2]) - (ct[0]*3600 + ct[1]*60 + ct[2])
print(f'{str((t//3600)%24).zfill(2)}:{str(t%3600//60).zfill(2)}:{str(t%3600%60).zfill(2)}')