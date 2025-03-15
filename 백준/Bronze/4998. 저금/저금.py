import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        inp = input()
        if inp == '':
            break
        N, B, M = map(float, inp.split())
        year = 0
        while 1:
            if N > M:
                break
            N += N*B/100
            year += 1
        print(year)


if __name__ == '__main__':
    main()