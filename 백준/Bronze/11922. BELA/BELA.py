import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, B = input().split()
    dap = 0
    dic = {'A':(11, 11), 'K':(4, 4), 'Q':(3, 3), 'J':(20, 2), 'T':(10, 10),
           '9':(14, 0), '8':(0, 0), '7':(0, 0)}
    for _ in range(4*int(N)):
        ki = input()
        a, b = ki[0], ki[1]
        dap += dic[a][0 if b == B else 1]
    print(dap)


if __name__ == '__main__':
    main()