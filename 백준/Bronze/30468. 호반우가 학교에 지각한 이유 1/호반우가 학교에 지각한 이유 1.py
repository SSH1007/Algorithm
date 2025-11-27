import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    Ns = list(map(int, input().split()))
    print(max(Ns[-1]*4 - sum(Ns[:4]), 0))


if __name__ == '__main__':
    main()