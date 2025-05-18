import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for t in range(1, T+1):
        B = int(input())*8
        case = input()
        dap = ''
        for b in range(0, B, 8):
            tmp = ''
            for i in range(b, b+8):
                tmp += ('1' if case[i] == 'I' else '0')
            dap += chr(int(tmp, 2))
        print(f'Case #%d: %s' % (t, dap))


if __name__ == '__main__':
    main()