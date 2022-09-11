def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

N = int(input())
lst = list(map(int, input().split()))
std = lst[0]
for l in range(1,len(lst)):
    print(f'{std//gcd(std,lst[l])}/{lst[l]//gcd(std,lst[l])}')