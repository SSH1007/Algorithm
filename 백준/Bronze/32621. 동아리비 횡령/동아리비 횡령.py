import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    lst = input().split('+')
    c = 0
    if len(lst) >= 2:
        if lst[0].isdigit() and lst[1].isdigit():
            if lst[0][0] != '0' and lst[1][0] != '0':
                if lst[0] == lst[1]:
                    c = 1
    print('CUTE' if c else 'No Money')


if __name__ == '__main__':
    main()