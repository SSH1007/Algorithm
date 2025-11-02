import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        A = list(map(int, input().split()))
        dap = 0
        for i in range(1, n):
            tmp = A[i]
            for j in range(i):
                if tmp >= A[j]:
                    dap += 1
        print(dap)


if __name__ == '__main__':
    main()