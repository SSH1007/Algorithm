ar = []
for _ in range(2):
    a,b,c,d,e = map(int, input().split())
    ar.append(a*6+b*3+c*2+d*1+e*2)
print(*ar)