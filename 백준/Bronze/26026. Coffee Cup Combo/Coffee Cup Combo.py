import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lec = list(map(int, list(input())))
    coffee = 0
    dap = 0
    for i in range(N):
        if lec[i] == 1:
            coffee = 2
            dap += 1
        else:
            if coffee > 0:
                coffee -= 1
                dap += 1
    print(dap)


if __name__ == '__main__':
    main()