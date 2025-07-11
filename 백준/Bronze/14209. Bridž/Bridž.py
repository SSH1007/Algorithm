import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dap = 0
    dic = {'A':4, 'K':3, 'Q':2, 'J':1, 'X':0}
    for _ in range(N):
        C = input()
        for c in C:
            dap += dic[c]
    print(dap)


if __name__ == '__main__':
    main()