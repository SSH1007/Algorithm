import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    As, Bs = [0]*N, [0]*N
    for n in range(N):
        A, B = map(int, input().split())
        As[n] = A
        Bs[n] = B
    for _ in range(M):
        K = int(input())
        for n in range(N):
            if As[n] <= K:
                As[n], Bs[n] = Bs[n], As[n]
    print(sum(As))


if __name__ == '__main__':
    main()