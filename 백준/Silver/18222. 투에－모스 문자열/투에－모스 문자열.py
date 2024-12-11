import sys
input = lambda: sys.stdin.readline().rstrip()


def F(k):
    if k == 1:
        return False
    x = 1
    while x+x < k:
        x += x
    return not F(k-x)


print(1 if F(int(input())) else 0)