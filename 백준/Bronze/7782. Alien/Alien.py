import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    b1, b2 = map(int, input().split())
    for _ in range(n):
        lx, ly, hx, hy = map(int, input().split())
        if lx <= b1 <= hx and ly <= b2 <= hy:
            print('Yes')
            return
    else:
        print('No')


if __name__ == '__main__':
    main()