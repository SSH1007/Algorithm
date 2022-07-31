n=int(input())
while 1:
    a = input()
    if a == '=':
        break
    b = int(input())
    n = int(eval('n'+a+'b'))
print(n)