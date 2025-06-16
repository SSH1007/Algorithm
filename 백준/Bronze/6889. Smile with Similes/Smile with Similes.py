import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    m = int(input())
    ns = list(input() for _ in range(n))
    ms = list(input() for _ in range(m))
    for i in ns:
        for j in ms:
            print(f'{i} as {j}')


if __name__ == '__main__':
    main()