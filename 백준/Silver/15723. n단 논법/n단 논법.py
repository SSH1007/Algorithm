import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    maps = [[0]*26 for _ in range(26)]
    for _ in range(N):
        a, _is, b = input().split()
        a, b = ord(a)-97, ord(b)-97
        maps[a][b] = 1

    for k in range(26):
        for i in range(26):
            for j in range(26):
                if maps[i][k] and maps[k][j]:
                    maps[i][j] = 1

    M = int(input())
    for _ in range(M):
        a, _is, b = input().split()
        a, b = ord(a)-97, ord(b)-97
        print('T' if maps[a][b] == 1 else 'F')


if __name__ == '__main__':
    main()