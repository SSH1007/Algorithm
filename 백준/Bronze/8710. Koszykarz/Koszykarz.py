k, w, m = map(int, input().split())
cha = (w-k)
if cha%m:
    print(cha//m+1)
else:
    print(cha//m)