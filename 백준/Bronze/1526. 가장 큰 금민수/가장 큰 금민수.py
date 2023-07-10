N = int(input())
while 1:
    S = set(str(N))
    if S == {'4', '7'} or S == {'4'} or S == {'7'}:
        print(N)
        break
    N -= 1