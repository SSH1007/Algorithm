import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        a, b = n//5, n%5
        for _ in range(a):
            print('++++ ', end='')
        print('|'*b)


if __name__ == '__main__':
    main()