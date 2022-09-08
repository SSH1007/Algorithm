a,b = map(int, input().split())
chicken = int(input())
if (a+b) >= chicken*2:
    print((a+b)-chicken*2)
else:
    print(a+b) 