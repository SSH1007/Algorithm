import sys
input = sys.stdin.readline


def main():
    N, H = map(int, input().rstrip().split())
    imos = [0]*(H+1)
    for n in range(N):
        size = int(input().rstrip())
        if not n % 2:
            imos[H-size] += 1
            imos[H] -= 1
        else:
            imos[0] += 1
            imos[size] -= 1

    now = 0
    for i in range(H+1):
        now += imos[i]
        imos[i] = now
    minV = min(imos[:-1])
    minCnt = imos[:-1].count(minV)
    print(minV, minCnt)


if __name__ == '__main__':
    main()