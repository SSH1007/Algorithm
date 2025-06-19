import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dic = {0:2, 1:1, 2:1/2, 4:1/4, 8:1/8, 16:1/16}
    _ = int(input())
    lst = list(map(int, input().split()))
    print(sum(dic[l] for l in lst))


if __name__ == '__main__':
    main()