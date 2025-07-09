import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    lst = list(input().split('('))
    print(lst[0])
    if len(lst) > 1:
        print(lst[1][:-1])
    else:
        print('-')


if __name__ == '__main__':
    main()