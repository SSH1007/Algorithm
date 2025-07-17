import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        S = input()
        S = S.replace('PO', 'PHO')
        print(S)


if __name__ == '__main__':
    main()