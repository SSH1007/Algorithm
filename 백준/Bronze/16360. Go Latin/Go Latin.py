import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        S = input()
        if S[-1] == 'a':
            print(S+'s')
        elif S[-1] == 'i' or S[-1] == 'y':
            print(S[:-1]+'ios')
        elif S[-1] == 'l':
            print(S+'es')
        elif S[-1] == 'n':
            print(S[:-1]+'anes')
        elif S[-2:] == 'ne':
            print(S[:-2]+'anes')
        elif S[-1] == 'o':
            print(S+'s')
        elif S[-1] == 'r':
            print(S+'es')
        elif S[-1] == 't':
            print(S+'as')
        elif S[-1] == 'u':
            print(S+'s')
        elif S[-1] == 'v':
            print(S+'es')
        elif S[-1] == 'w':
            print(S+'as')
        else:
            print(S+'us')


if __name__ == '__main__':
    main()