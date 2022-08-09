def cdg(a,b):
    while 1:
        if a%b==0:
            return b
        a,b=b,a%b
        
a,b = map(int,input().split())
print(cdg(a,b))
print(a*b//cdg(a,b))