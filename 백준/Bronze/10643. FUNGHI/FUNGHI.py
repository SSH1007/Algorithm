import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    pizza = [int(input()) for _ in range(8)]
    dap = 0
    for i in range(8):
        tmp = 0
        for j in range(4):
            idx = (i+j)%8
            tmp += pizza[idx]
        dap = max(dap, tmp)
    print(dap)


if __name__ == '__main__':
    main()