import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    _ = int(input())
    Fs = list(map(int, input().split()))
    if sum(Fs) >= T:
        print('Padaeng_i Happy')
    else:
        print('Padaeng_i Cry')


if __name__ == '__main__':
    main()