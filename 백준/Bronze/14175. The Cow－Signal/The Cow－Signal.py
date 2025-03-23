import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    M, N, K = map(int, input().split())
    for _ in range(M):
        S = input()
        for _ in range(K):
            for s in S:
                print(s*K,end='')
            print()


if __name__ == '__main__':
    main()