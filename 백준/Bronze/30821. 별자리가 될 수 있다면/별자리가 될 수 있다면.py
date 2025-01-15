import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    tmp = 1
    for i in range(N-4, N+1):
        tmp *= i
    print(tmp//120)


if __name__ == '__main__':
    main()