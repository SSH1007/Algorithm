import sys
input = sys.stdin.readline
n = int(input().rstrip())
for i in range(n):
    if i:
        print()
    a, b, c = map(int, input().rstrip().split())
    print(f'Data set: {a} {b} {c}')
    for _ in range(c):
        if a>b:
            a = a//2
        else:
            b = b//2
    if a>b:
        print(a,b)
    else:
        print(b,a)