import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, A, B = map(int, input().split())
    a, b = 1, 1
    for _ in range(N):
        a += A
        b += B
        if a < b:
            a, b = b, a
        elif a == b:
            b -= 1
    print(a, b)


if __name__ == '__main__':
    main()