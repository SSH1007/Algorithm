import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    J, N = map(int, input().split())
    dap = 0
    for _ in range(N):
        Q = input()
        tmp = 0
        for q in Q:
            if q.isalpha():
                if ord(q) > 90:
                    tmp += 2
                else:
                    tmp += 4
            elif q.isdigit():
                tmp += 2
            else:
                tmp += 1
        if tmp <= J:
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()