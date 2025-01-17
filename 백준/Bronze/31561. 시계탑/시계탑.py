import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    M = int(input())
    if M <= 30:
        print(M/2)
    else:
        print(15+(M-30)*(3/2))


if __name__ == '__main__':
    main()