import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    M = input()
    K = int(input())
    if K == 0:
        print('YES')
        exit(0)
    if '1' in M[-K:]:
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    main()