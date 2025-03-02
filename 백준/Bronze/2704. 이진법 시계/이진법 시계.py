import sys
input = lambda: sys.stdin.readline().rstrip()


def B(n):
    d = bin(n)[2:]
    return d.zfill(6)

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