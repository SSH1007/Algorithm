import sys
input = lambda: sys.stdin.readline().rstrip()
from datetime import date, timedelta


def main():
    N = int(input())
    start_date = date(2014, 4, 2)
    future_date = start_date + timedelta(days=N-1)
    print(future_date)


if __name__ == '__main__':
    main()