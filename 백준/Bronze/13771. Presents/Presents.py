import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = [float(input()) for _ in range(N)]
    lst.sort()
    print(f'%.2f' % lst[1])


if __name__ == '__main__':
    main()