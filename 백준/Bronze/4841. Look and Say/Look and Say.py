import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        S = input() + ' '
        s, e = 0, 0
        dap, now, cnt = '', '', 0
        while e < len(S):
            now = S[s]
            if S[s] != S[e]:
                dap = dap + str(cnt) + now
                s = e
                cnt = 0
            else:
                cnt += 1
                e += 1
        print(dap)


if __name__ == '__main__':
    main()