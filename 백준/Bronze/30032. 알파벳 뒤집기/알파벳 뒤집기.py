import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, D = map(int, input().split())
    maps = [list(input()) for _ in range(N)]
    dic = {'d': ['q', 'b'], 'b': ['p', 'd'], 'q': ['d', 'p'], 'p': ['b', 'q']}

    for r in range(N):
        for c in range(N):
            maps[r][c] = dic[maps[r][c]][(D+1) % 2]
    for n in range(N):
        print(''.join(maps[n]))


if __name__ == '__main__':
    main()