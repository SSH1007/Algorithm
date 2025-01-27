import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    W = int(input())
    print(int((W//2)**0.5)*8)


if __name__ == '__main__':
    main()