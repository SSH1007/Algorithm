import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dap = 0
    tmp = 'PER'
    S = input()
    for i in range(len(S)):
        if S[i] != tmp[i%3]:
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()