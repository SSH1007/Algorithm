import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    a, b, c = 0, 1, 0
    while a < N:
        a += b
        b += 1
        c += 1
    if c%2 == 0:
        if a == N:
            print(b)
        else:
            print(0)
    else:
        print(a-N)


if __name__ == '__main__':
    main()