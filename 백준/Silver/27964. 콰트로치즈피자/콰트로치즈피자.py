import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dic = dict()
    lst = list(input().split())
    for l in lst:
        if len(l)>=6 and l[-6:] == 'Cheese':
            dic[l[:-6]] = 1
    if len(dic) >= 4:
        print('yummy')
    else:
        print('sad')


if __name__ == '__main__':
    main()