import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    dap = 0
    for i in range(N+1):
        if K == i//10 or K == i%10:
            dap += 3600
            continue
        for j in range(60):
            if K == j//10 or K == j%10:
                dap += 60
                continue
            for k in range(60):
                if K == k//10 or K == k%10:
                    dap += 1
    print(dap)


if __name__ == '__main__':
    main()