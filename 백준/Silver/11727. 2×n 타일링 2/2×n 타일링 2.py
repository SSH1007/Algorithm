n = int(input())
lst = [0]*(n+1)
lst[1] = 1
for i in range(2,n+1):
    if i%2:
        lst[i]=lst[i-1]*2-1
    else:
        lst[i]=lst[i-1]*2+1
print(lst[n]%10007)