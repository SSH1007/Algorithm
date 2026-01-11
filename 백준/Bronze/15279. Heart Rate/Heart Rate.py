import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        b, p = map(float, input().split())
        print(f'{60*(b-1)/p:.4f} {60*b/p:.4f} {60*(b+1)/p:.4f}')


if __name__ == '__main__':
    main()