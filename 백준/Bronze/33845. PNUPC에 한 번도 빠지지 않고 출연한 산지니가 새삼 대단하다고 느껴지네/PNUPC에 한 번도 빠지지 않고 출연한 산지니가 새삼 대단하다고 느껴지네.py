import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = set(input())
    T = input()
    dap = ''
    for t in T:
        if t not in S:
            dap += t
    print(dap)


if __name__ == '__main__':
    main()