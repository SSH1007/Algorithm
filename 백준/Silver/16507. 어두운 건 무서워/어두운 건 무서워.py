import sys
input = sys.stdin.readline


def main():
    R, C, Q = map(int, input().rstrip().split())
    info = [list(map(int, input().rstrip().split())) for _ in range(R)]
    prefix = [[0]*(C+1) for _ in range(R+1)]
    for r in range(1, R+1):
        for c in range(1, C+1):
            prefix[r][c] = info[r-1][c-1] + prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1]

    for _ in range(Q):
        r1, c1, r2, c2 = map(int, input().rstrip().split())
        lightSum = prefix[r2][c2]-prefix[r2][c1-1]-prefix[r1-1][c2]+prefix[r1-1][c1-1]
        lightCnt = (r2-r1+1)*(c2-c1+1)
        print(lightSum//lightCnt)


if __name__ == '__main__':
    main()