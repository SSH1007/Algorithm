import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    Ms = list(map(int, input().split()))
    maps = [list(map(int, input().split())) for _ in range(N)]
    dap = 0
    for i in range(1, M):
        dap += maps[Ms[i-1]-1][Ms[i]-1]
    print(dap)


if __name__ == '__main__':
    main()