import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dap, std = '', 0
    while 1:
        info = input().split()
        city, tpr = info[0], int(info[1])
        if std > tpr:
            dap = city
            std = tpr
        if city == 'Waterloo':
            break
    print(dap)


if __name__ == '__main__':
    main()