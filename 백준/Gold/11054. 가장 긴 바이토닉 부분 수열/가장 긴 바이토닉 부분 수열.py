import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    As = list(map(int, input().split()))
    # 가장 짧은 부분 수열의 길이는 1
    inc = [1 for _ in range(N)]
    dec = [1 for _ in range(N)]
    
    for i in range(N):
        for j in range(i):
            if As[i] > As[j]:
                inc[i] = max(inc[i], inc[j]+1)
    for i in range(N, -1, -1):
        for j in range(i, N):
            if As[i] > As[j]:
                dec[i] = max(dec[i], dec[j]+1)

    dap = -1
    for i in range(N):
        dap = max(dap, inc[i]+dec[i])
    print(dap-1)


if __name__ == '__main__':
    main()