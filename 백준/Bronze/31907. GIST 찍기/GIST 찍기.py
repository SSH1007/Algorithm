import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        print('G'*N+'.'*N*3)
    for _ in range(N):
        print('.'*N+'I'*N+'.'*N+'T'*N)
    for _ in range(N):
        print('.'*N*2+'S'*N+'.'*N)


if __name__ == '__main__':
    main()