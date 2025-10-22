import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for n in range(1, N+1):
        lst = list(input().split())
        dap = ' '.join(lst[::-1])
        print(f'Case #{n}: {dap}')


if __name__ == '__main__':
    main()