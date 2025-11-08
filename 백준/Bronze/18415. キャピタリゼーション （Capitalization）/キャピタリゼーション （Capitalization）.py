import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S = input()
    s, d = 0, ''
    while s < N:
        if S[s:s+3] == 'joi':
            d = d + 'JOI'
            s += 3
        else:
            d += S[s]
            s += 1
    print(d)


if __name__ == '__main__':
    main()