import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    pi = 3.14159
    dap = 0.0
    for _ in range(int(input())):
        A, *B = input().split()
        if A == 'C':
            r, h = float(B[0]), float(B[1])
            dap = max(dap, (1/3)*pi*r*r*h)
        elif A == 'L':
            r, h = float(B[0]), float(B[1])
            dap = max(dap, pi*r*r*h)
        else:
            r = float(B[0])
            dap = max(dap, (4/3)*pi*r*r*r)
    print(f'{dap:.3f}')


if __name__ == '__main__':
    main()