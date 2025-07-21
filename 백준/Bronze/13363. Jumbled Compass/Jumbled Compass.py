import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    A = int(input())
    B = int(input())
    cw = (B-A+360)%360
    ccw = (A-B+360)%360
    if cw <= ccw:
        print(cw)
    else:
        print(-ccw)


if __name__ == '__main__':
    main()