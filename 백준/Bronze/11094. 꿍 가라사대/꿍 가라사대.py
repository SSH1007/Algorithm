import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        S = input()
        if S[:10] == 'Simon says':
            print(S[10:])


if __name__ == '__main__':
    main()