hap, cha = map(int, input().split())
a= (hap+cha)/2
b= hap-a

if int(a)==a and int(b) == b and a>=0 and b>=0:
    print(int(max(a,b)), int(min(a,b)))
else:
    print(-1) 