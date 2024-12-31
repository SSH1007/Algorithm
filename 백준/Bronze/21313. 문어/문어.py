import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    i, odd = 0, 0
    if N%2:
        odd = 1
        N -= 1
    while N:
        if N%2:
            print(2, end=' ')
        else:
            print(1, end=' ')
        N -= 1
    if odd:
        print(3)


if __name__ == '__main__':
    main()