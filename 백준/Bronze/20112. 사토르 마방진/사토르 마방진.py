import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = [list(input()) for _ in range(N)]
    r_lst = list(map(list, zip(*lst)))
    for n in range(N):
        if lst[n] != r_lst[n]:
            print('NO')
            return
    else:
        print('YES')


if __name__ == '__main__':
    main()