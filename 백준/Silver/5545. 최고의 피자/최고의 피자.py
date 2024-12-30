import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A, B = map(int, input().split())
    C = int(input())
    lst = [int(input()) for _ in range(N)]
    lst.sort(reverse=True)
    dap, cal, fee = C//A, C, A
    for l in lst:
        cal += l
        fee += B
        dap = max(dap, cal//fee)
    print(dap)


if __name__ == '__main__':
    main()