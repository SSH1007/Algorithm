import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, S = input().split()
    dap = 0
    for _ in range(int(N)):
        name, quantity = input().split()
        lst = name.split('_')
        for l in lst:
            if l == S:
                dap += int(quantity)
                break
    print(dap)


if __name__ == '__main__':
    main()