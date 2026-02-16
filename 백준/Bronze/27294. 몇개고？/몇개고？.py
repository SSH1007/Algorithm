import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T, S = map(int, input().split())
    if S or (T < 12 or T > 16):
        print(280)
    if not S and (12 <= T <= 16):
        print(320)


if __name__ == '__main__':
    main()