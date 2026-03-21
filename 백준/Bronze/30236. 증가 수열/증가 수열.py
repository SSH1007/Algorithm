import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        d = 1
        n = int(input())
        a = list(map(int, input().split()))
        b = [0]
        for i in range(n):
            while 1:
                if d != a[i] and b[-1] < d:
                    break
                d += 1
            b.append(d)
        print(b[-1])


if __name__ == '__main__':
    main()