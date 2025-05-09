import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dic = {'Paper': 57.99, 'Printer': 120.50, 'Planners': 31.25, 'Binders': 22.50, 'Calendar': 10.95, 'Notebooks': 11.20, 'Ink': 66.95}
    dap = 0
    while 1:
        I = input()
        if I == 'EOI':
            break
        dap += dic[I]
    print('$', dap, sep='')


if __name__ == '__main__':
    main()