import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    D, M = map(int, input().split())
    dic = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
    mth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ((D-1)+sum([mth[i] for i in range(M)]))%7
    print(dic[day])


if __name__ == '__main__':
    main()