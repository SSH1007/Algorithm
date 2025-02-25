import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    cur = 1
    maps = [0]+[int(input()) for _ in range(N)]
    for j in range(1, M+1):
        D = int(input())
        cur += D
        if cur >= N:
            break
        cur += maps[cur]
        if cur >= N:
            break
    print(j)


if __name__ == '__main__':
    main()