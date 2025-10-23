import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    while 1:
        n += 1
        if '0' not in str(n):
            break
    print(n)


if __name__ == '__main__':
    main()