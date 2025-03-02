import sys
input = lambda: sys.stdin.readline().rstrip()


def B(n):
    d = bin(int(n))[2:]
    return d.zfill(6)


def main():
    N = int(input())
    for _ in range(N):
        H, M, S = map(B, input().split(":"))
        R = H + M + S
        C = "".join([h+m+s for h,m,s in zip(H, M, S)])
        print(C+' '+R)


if __name__ == '__main__':
    main()