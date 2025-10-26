import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    K = int(input())
    if K in [2, 4, 6, 8]:
        print(0)
    else:
        print(8)


if __name__ == '__main__':
    main()