# 1 집합과 0 집합의 각 개수를 센 뒤, 최소값을 출력하면 된다.
S = input()
one = S.split('0')
zero = S.split('1')
oN, zN = 0,0
for o in one:
    if o!='':
        oN+=1
for z in zero:
    if z!='':
        zN+=1
print(min(oN, zN))