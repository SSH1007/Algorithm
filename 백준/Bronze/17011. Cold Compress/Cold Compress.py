import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        S = input() + ' '
        L = len(S)
        lst = []
        cnt = 1
        for l in range(L-1):
            if S[l] != S[l+1]:
                lst.append(str(cnt))
                lst.append(S[l])
                cnt = 1
            else:
                cnt += 1
        print(' '.join(lst))


if __name__ == '__main__':
    main()