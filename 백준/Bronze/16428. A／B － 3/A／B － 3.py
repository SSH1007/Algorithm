a, b = map(int, input().split())
if a == 0:
    print(0)
    print(0)
elif b > 0:
    print(a//b)
    print(a%b)
elif a > 0 and b < 0:
    print(a//abs(b)*-1)
    print(a % abs(b))
elif a < 0 and b < 0:
    print(a//abs(b)*-1)
    print(a%abs(b))