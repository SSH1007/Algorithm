import sys
input = lambda: sys.stdin.readline().rstrip()


def hap(n):
    res = 0
    while n:
        res += n%10
        n//=10
    return res


def main():
    S = input()
    for s in S:
        print(s*hap(ord(s)))


if __name__ == '__main__':
    main()