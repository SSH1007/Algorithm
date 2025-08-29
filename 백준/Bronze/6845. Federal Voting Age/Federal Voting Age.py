import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    ey, em, ed = 2007, 2, 27
    for _ in range(N):
        y, m, d = map(int, input().split())
        age = ey-y
        if (m, d) > (em, ed):
            age -= 1
        print('Yes' if age >= 18 else 'No')


if __name__ == '__main__':
    main()