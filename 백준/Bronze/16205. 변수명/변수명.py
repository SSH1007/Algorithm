import sys
input = lambda: sys.stdin.readline().rstrip()


def F(o, n, S):
    if o == n:
        return S
    else:
        if o == 1:
            d = S[0].lower()
            for i in range(1, len(S)):
                if S[i-1] == '_':
                    d += S[i].upper()
                elif S[i] != '_':
                    d += S[i]
            return d
        elif o == 2:
            d = S[0].lower()
            for i in range(1, len(S)):
                if S[i].isupper():
                    d += '_'
                d += S[i].lower()
            return d
        else:
            d = S[0].upper()
            flag = 0
            for i in range(1, len(S)):
                if S[i] == '_':
                    flag = 1
                elif flag:
                    d += S[i].upper()
                    flag = 0
                else:
                    d += S[i]
            return d


def main():
    N, S = input().split()
    print(F(1, int(N), S))
    print(F(2, int(N), S))
    print(F(3, int(N), S))


if __name__ == '__main__':
    main()