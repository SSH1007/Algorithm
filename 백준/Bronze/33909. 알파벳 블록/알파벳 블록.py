import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    s, c, o, n = map(int, input().split())
    s += n
    c += o*2
    print(min(s//3, c//6))


if __name__ == '__main__':
    main()