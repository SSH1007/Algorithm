import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    lst = sorted(list(map(int, input().split())))
    ABC = lst[-1]
    A = ABC-lst[-2]
    B = ABC-lst[-3]
    print(A, B, ABC-A-B)


if __name__ == '__main__':
    main()