import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    C = float(input())
    L = int(input())
    dap = 0
    for _ in range(L):
        w, l = map(float, input().split())
        dap += w*l*C
    print(dap)


if __name__ == '__main__':
    main()