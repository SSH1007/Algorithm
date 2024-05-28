import sys
input = sys.stdin.readline


def square(num):
    if (int(num)**0.5) % 1:
        return False
    else:
        return True


def main():
    N, M = map(int, input().rstrip().split())
    pan = [list(input().rstrip()) for _ in range(N)]
    dap = -1
    for n in range(N):
        for m in range(M):
            for n_cha in range(-N, N+1):
                for m_cha in range(-M, M+1):
                    r, c = n, m
                    tmp = ''
                    if n_cha == 0 and m_cha == 0:
                        continue
                    while 0 <= r < N and 0 <= c < M:
                        tmp += pan[r][c]
                        if square(tmp):
                            dap = max(dap, int(tmp))
                        r += n_cha
                        c += m_cha
    print(dap)
    return


if __name__ == '__main__':
    main()