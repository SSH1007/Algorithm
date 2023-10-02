T = int(input())
for _ in range(T):
    num, bit = map(int, input().split())
    bnum = bin(num)
    bnum = bnum[2:].zfill(16)
    cnt = bnum.count('1')
    a = cnt%2
    b = bit%2
    if a == b:
        print('Valid')
    else:
        print('Corrupt')