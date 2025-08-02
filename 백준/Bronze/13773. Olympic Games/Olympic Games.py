import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        N = int(input())
        if N == 0:
            break
        print(N, end=' ')
        if N >= 1896 and (N-1896) % 4 == 0:
            if N > 2020:
                print('No city yet chosen')
            elif 1914 <= N <= 1918 or 1939 <= N <= 1945:
                print('Games cancelled')
            else:
                print('Summer Olympics')
        else:
            print('No summer games')


if __name__ == '__main__':
    main()