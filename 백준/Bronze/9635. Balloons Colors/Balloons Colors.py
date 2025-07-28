import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        N, X, Y = map(int, input().split())
        lst = list(map(int, input().split()))
        if lst[0] == X and lst[-1] == Y:
            print('BOTH')
        elif lst[0] != X and lst[-1] != Y:
            print('OKAY')
        elif lst[0] == X:
            print('EASY')
        else:
            print('HARD')


if __name__ == '__main__':
    main()