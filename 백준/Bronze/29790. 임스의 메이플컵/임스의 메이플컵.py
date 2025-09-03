import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, U, L = map (int, input().split())
    if N >= 1000:
        if U >= 8000 or L>= 260:
            print('Very Good')
        else:
            print('Good')
    else:
        print('Bad')


if __name__ == '__main__':
    main()