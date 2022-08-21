N = int(input())
lst = [1,1]
for i in range(N+1):
    if i <= 1:
        pass
    else:
        lst.append(lst[i-1]*i)
Nstr = str(lst[N])
Nlen = len(Nstr)
cnt = 0
for i in range(Nlen):
    if Nstr[Nlen-i-1] != '0':
        break
    cnt += 1
print(cnt)