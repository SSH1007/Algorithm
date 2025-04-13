import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    As = list(map(int, input().split()))
    X, Y = map(int, input().split())
    tmp = 0
    for a in As:
        if Y <= a:
            tmp += 1
    print(N*X//100, tmp)


if __name__ == '__main__':
    main()