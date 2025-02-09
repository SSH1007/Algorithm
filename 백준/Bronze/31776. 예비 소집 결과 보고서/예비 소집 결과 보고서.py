import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dap = 0
    for _ in range(N):
        Ts = list(map(int, input().split()))
        if Ts[0] >= 0:
            if Ts[1] >= Ts[0]:
                if Ts[2] >= Ts[1] or Ts[2] == -1:
                    dap += 1
            elif Ts[1] == -1:
                if Ts[2] == -1:
                    dap += 1
    print(dap)


if __name__ == '__main__':
    main()