import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    v = '****************.**.**..*.**..*******..*.*****.**.**..*.**..*.*************'
    N = int(input())
    S = input()
    for i in range(5):
        for n in range(N):
            t = ord(S[n])-65
            print(v[i*15:i*15+15][t*3:t*3+3], end='')
        print()


if __name__ == '__main__':
    main()