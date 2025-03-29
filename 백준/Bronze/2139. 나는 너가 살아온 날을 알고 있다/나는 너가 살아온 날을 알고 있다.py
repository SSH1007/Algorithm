import sys
input = lambda: sys.stdin.readline().rstrip()


def leap(n):
    if (n%4 == 0 and n%100) or n%400==0:
        return True
    else:
        return False


def main():
    month = [0,0,31,59,90,120,151,181,212,243,273,304,334]
    leap_month = [0,0,31,60,91,121,152,182,213,244,274,305,335]
    while 1:
        d, m, y = map(int, input().split())
        if d == 0 and m == 0 and y == 0:
            break
        if leap(y):
            print(leap_month[m]+d)
        else:
            print(month[m]+d)


if __name__ == '__main__':
    main()
