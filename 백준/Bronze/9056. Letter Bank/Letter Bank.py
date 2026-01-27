import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    for _ in range(int(input())):
        a, b = map(set, input().split())
        print('YES' if a == b else 'NO')


if __name__ == '__main__':
    main()