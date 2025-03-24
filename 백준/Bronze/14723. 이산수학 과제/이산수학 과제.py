import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    if N <= 2:
        print(N, 1)
        exit(0)
    s, i = 0, 1
    for i in range(1, N):
        s += i
        if N <= s:
            break
    a, b = i, 1
    for _ in range(N-(s-i)-1):
        a -= 1
        b += 1
    print(a, b)


if __name__ == '__main__':
    main()