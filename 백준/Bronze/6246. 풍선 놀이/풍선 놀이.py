import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, Q = map(int, input().split())
    balloon = [0]*(N+1)
    for _ in range(Q):
        L, I = map(int, input().split())
        for i in range(L, N+1, I):
            balloon[i] = 1
    print(balloon.count(0)-1)


if __name__ == '__main__':
    main()