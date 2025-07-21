import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dap = 2
    cnt = 0
    S1 = input()
    S2 = input()
    for i in range(4):
        if S1[i] != S2[i]:
            cnt += 1
    print(dap**cnt)


if __name__ == '__main__':
    main()