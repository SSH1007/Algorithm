import sys
input = lambda: sys.stdin.readline().rstrip()


def B(n):
    dap = ''
    while n!=0:
        dap = str(n%2) + dap
        n//=2
    for i in range(6-len(dap)):
        dap = '0' + dap
    return dap


def main():
    N = int(input())
    for _ in range(N):
        H, M, S = map(int, input().split(":"))
        R = B(H) + B(M) + B(S)
        C = ''
        for i in range(6):
            for j in range(i, 18, 6):
                C += R[j]
        print(C+' '+R)


if __name__ == '__main__':
    main()