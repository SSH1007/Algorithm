import sys
input = lambda: sys.stdin.readline().rstrip()


def F(S):
    l = len(S)
    d = 0
    for s in S:
        d += int(s)
    return d*l


def main():
    A, B = input().split()
    a, b = F(A), F(B)
    if a > b:
        print(1)
    elif a < b:
        print(2)
    else:
        print(0)


if __name__ == '__main__':
    main()