import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    a%=10
    if a == 0:
        a = 10
    if a == 1 or a == 5 or a == 6 or a == 10:
        print(a)
    elif a == 4:
        b = b%2
        lst = [6,4]
        print((lst[b]))
    elif a == 9:
        b = b%2
        lst = [1,9]
        print((lst[b]))
    elif a == 2:
        b = b%4
        lst = [6,2,4,8]
        print((lst[b]))
    elif a == 3:
        b = b%4
        lst = [1,3,9,7]
        print((lst[b]))
    elif a == 7:
        b = b%4
        lst = [1,7,9,3]
        print((lst[b]))
    elif a == 8:
        b = b%4
        lst = [6,8,4,2]
        print((lst[b]))