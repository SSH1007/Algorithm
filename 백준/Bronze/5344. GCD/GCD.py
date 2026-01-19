import sys
input = lambda: sys.stdin.readline().rstrip()


def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def main():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(GCD(a, b))


if __name__ == '__main__':
    main()