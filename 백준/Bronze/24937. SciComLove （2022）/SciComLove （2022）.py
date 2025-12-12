import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    print("SciComLove"[N%10:]+"SciComLove"[:N%10])


if __name__ == '__main__':
    main()