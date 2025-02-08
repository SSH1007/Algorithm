import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        S = input()
        print(S[::-1])


if __name__ == '__main__':
    main()