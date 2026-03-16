import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, B, H, W = map(int, input().split())
    inf = float('inf')
    dap = inf
    for _ in range(H):
        p = int(input())
        As = list(map(int, input().split()))
        for a in As:
            if a >= N and N*p <= B:
                dap = min(dap, N*p)
    print('stay home' if dap == inf else dap)


if __name__ == '__main__':
    main()