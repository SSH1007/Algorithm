import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        lst = set(map(int, input().split()))
        if lst == {0, 1, 4, 5} or lst == {4, 5, 6, 7} or lst == {2, 3, 6, 7} or\
            lst == {0, 1, 2, 3} or lst == {1, 3, 5, 7} or lst == {0, 2, 4, 6}:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()