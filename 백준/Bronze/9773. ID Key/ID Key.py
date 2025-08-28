import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        S = input()
        a = 0
        for s in S:
            a += int(s)
        b = int(S[-3:])*10
        c = a+b
        if c > 9999:
            c %= 10000
        elif c < 1000:
            c += 1000
        print(str(c).zfill(4))


if __name__ == '__main__':
    main()