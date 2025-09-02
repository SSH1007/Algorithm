import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        a, b, c = input().split()
        a, b, c = float(a), float('0'+b), float('0'+c)
        dap = a*b*c
        print(f'${dap:.2f}')


if __name__ == '__main__':
    main()