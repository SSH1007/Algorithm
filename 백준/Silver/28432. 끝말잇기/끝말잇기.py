import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    Si = [input() for _ in range(N)]
    s, e = '', ''
    for n in range(N):
        if Si[n] == '?':
            if n > 0:
               s = Si[n-1][-1]
            if n < N-1:
                e = Si[n+1][0]
    M = int(input())
    Mi = [input() for _ in range(M)]
    if N == 1:
        print(Mi[0])
        exit(0)
    for m in range(M):
        if Mi[m] in Si:
            continue
        if s == '':
            if Mi[m][-1] == e:
                print(Mi[m])
                break
        elif e == '':
            if Mi[m][0] == s:
                print(Mi[m])
                break
        elif s != '' and e != '':
            if Mi[m][0] == s and Mi[m][-1] == e:
                print(Mi[m])
                break


if __name__ == '__main__':
    main()