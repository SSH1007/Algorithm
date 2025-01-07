import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S, E = 0, 10**5
    for _ in range(N):
        s, e = map(int, input().split())
        if S < s:
            S = s
        if E > e:
            E = e
    tmp = S-E
    if tmp < 0:
        print(0)
    else:
        print(tmp)


if __name__ == '__main__':
    main()