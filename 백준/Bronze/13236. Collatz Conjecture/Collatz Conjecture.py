n = int(input())
while 1:
    print(n, end=' ')
    if n == 1:
        break
    elif n%2:
        n*=3
        n+=1
    else:
        n//=2