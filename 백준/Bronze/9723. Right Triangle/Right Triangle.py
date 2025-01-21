import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for n in range(1, N+1):
        lst = list(map(int, input().split()))
        lst.sort()
        a, b, c = lst[0], lst[1], lst[2]
        print(f'Case #{n}:', end=' ')
        if c**2 == a**2 + b**2:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()