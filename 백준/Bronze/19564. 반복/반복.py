import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = input()
    dap = 1
    for i in range(1, len(S)):
        if ord(S[i-1]) >= ord(S[i]):
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()