import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    if T%2:
        print('still running')
        return
    dap, q = 0, 0
    for t in range(T):
        s = int(input())
        if t%2:
            dap += (s-q)
        else:
            q = s
    print(dap)


if __name__ == '__main__':
    main()