import sys
input = sys.stdin.readline


def main():
    first = input().rstrip()
    second = input().rstrip()
    F, S = len(first), len(second)
    maps = [[0]*(F+1) for _ in range(S+1)]

    dap = 0
    for s in range(1, S+1):
        for f in range(1, F+1):
            if first[f-1] == second[s-1]:
                maps[s][f] = maps[s-1][f-1]+1
                dap = max(dap, maps[s][f])

    print(dap)


if __name__ == '__main__':
    main()