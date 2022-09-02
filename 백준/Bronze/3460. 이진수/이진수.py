def bin(n):
    if n < 1:
        return ''
    a = n%2
    return bin(n//2) + str(a)

T = int(input())
for _ in range(T):
    n = int(input())
    a = bin(n)[::-1]
    for i in range(len(a)):
        if a[i]=='1':
            print(i, end=' ')