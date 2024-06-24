import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().rstrip().split())
    trains = [0 for _ in range(N)]
    for _ in range(M):
        info = list(map(int, input().rstrip().split()))
        if info[0] == 1:
            trains[info[1]-1] |= (1 << (info[2]-1))
        elif info[0] == 2:
            trains[info[1]-1] &= ~(1 << (info[2]-1))
        elif info[0] == 3:
            trains[info[1]-1] <<= 1
            trains[info[1]-1] &= ~(1 << 20)
        else:
            trains[info[1]-1] >>= 1

    dap = []
    for t in trains:
        if t not in dap:
            dap.append(t)
    print(len(dap))


if __name__ == '__main__':
    main()