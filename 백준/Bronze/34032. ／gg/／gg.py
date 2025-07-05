import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S = input()
    G = S.count('O')
    print('Yes' if G >= N-G else 'No')


if __name__ == '__main__':
    main()