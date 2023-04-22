import sys
input = sys.stdin.readline

while 1:
    n = int(input().rstrip())
    if n:
        while n>9:
            n = sum(map(int, str(n)))
        print(n)
    else:
        break