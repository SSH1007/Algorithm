import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = list(map(int, input().split()))
    s, e = 0, N-1
    std = lst[s]+lst[e]
    while s < e:
        if abs(lst[s]+lst[e]) < abs(std):
            std = lst[s]+lst[e]
        if lst[s]+lst[e] < 0:
            s += 1
        else:
            e -= 1
    print(std)


if __name__ == '__main__':
    main()