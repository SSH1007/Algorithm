import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    cnt = 1
    while 1:
        o, w = map(int, input().split())
        alive = 1
        if o == w == 0:
            break
        while 1:
            c, n = input().split()
            if c == '#':
                break
            n = int(n)
            if alive:
                if c == 'E':
                    w -= n
                elif c == 'F':
                    w += n
            if w <= 0:
                alive = 0
        if alive:
            if o*2 > w > o//2:
                print(f'{cnt} :-)')
            else:
                print(f'{cnt} :-(')
        else:
            print(f'{cnt} RIP')
        cnt += 1


if __name__ == '__main__':
    main()