import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for i in range(1, 10):
        if N % i == 0 and N // i <= 9:
            print(1)
            exit()
    else:
        print(0)


if __name__ == '__main__':
    main()