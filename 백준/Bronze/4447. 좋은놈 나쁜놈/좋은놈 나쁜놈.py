n=int(input())
for _ in range(n):
    a = input()
    b = a.lower()
    gcnt = b.count('g')
    bcnt = b.count('b')
    if gcnt>bcnt:
        print(f'{a} is GOOD')
    elif gcnt < bcnt:
        print(f'{a} is A BADDY')
    else:
        print(f'{a} is NEUTRAL')