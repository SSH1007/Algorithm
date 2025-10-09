import sys
input = lambda: sys.stdin.readline().rstrip()


def F(n, p):
    S = int(n)
    i, d = 0, 0
    while S > 0:
        d += (S%10) * (p**i)
        S //= 10
        i += 1
    return d


def main():
    for _ in range(int(input())):
        K, S = input().split()
        o, x = 0, 0
        if not '8' in S and not '9' in S:
            o = F(S, 8)
        x = F(S, 16)
        print(K, o, int(S), x)


if __name__ == '__main__':
    main()