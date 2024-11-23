import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = input()
    n, idx = 0, 0
    while 1:
        n += 1
        for s in str(n):
            if S[idx] == s:
                idx += 1
                if idx >= len(S):
                    print(n)
                    return


if __name__ == '__main__':
    main()