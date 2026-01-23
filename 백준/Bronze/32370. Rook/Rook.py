import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    a, b = map(int, input().split())
    x, y = map(int, input().split())
    dap = 2
    if a == 0:
        if x != 0: dap = 1
        elif y < b: dap = 3
        else: dap = 1
    elif b == 0:
        if y != 0: dap = 1
        elif x < a: dap = 3
        else: dap = 1
    print(dap)


if __name__ == '__main__':
    main()