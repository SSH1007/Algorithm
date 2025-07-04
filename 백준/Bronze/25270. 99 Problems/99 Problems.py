import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    if N > 99:
        t1, c1, t2, c2 = N, 0, N, 0
        while 1:
            if t1 % 100 == 99:
                break
            t1 -= 1
            c1 += 1
        while 1:
            if t2 % 100 == 99:
                break
            t2 += 1
            c2 += 1
        print(t2 if c2 <= c1 else t1)
    else:
        print(99)


if __name__ == '__main__':
    main()