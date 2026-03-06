import sys
input = lambda: sys.stdin.readline().rstrip()


def F(S, A):
    W = (S*S)/((S*S)+(A*A))
    return W


def main():
    T = int(input())
    inf = float('inf')
    for _ in range(T):
        n, m = map(int, input().split())
        lst = [[0]*(n+1) for _ in range(3)]
        for _ in range(m):
            a, b, p, q = map(int, input().split())
            lst[0][a] += 1
            lst[1][a] += p
            lst[2][a] -= q
            lst[0][b] += 1
            lst[1][b] += q
            lst[2][b] -= p
        mx, mn = -inf, inf
        for i in range(1, n+1):
            if lst[1][i] == 0 and lst[2][i] == 0:
                tmp = 0
            else:
                tmp = F(lst[1][i], lst[2][i])
            mx = max(mx, tmp)
            mn = min(mn, tmp)
        print(int(mx*1000))
        print(int(mn*1000))


if __name__ == '__main__':
    main()