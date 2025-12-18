import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        a, b = 0, 100000
        for _ in range(N):
            W, C = map(int, input().split())
            tmp = W/C
            if a < tmp:
                a = tmp
                b = C
            elif a == tmp:
                a = tmp
                b = min(b, C)
        print(b)


if __name__ == '__main__':
    main()