import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    a = 2**((N+1)//2)
    print(a%16769023)


if __name__ == '__main__':
    main()