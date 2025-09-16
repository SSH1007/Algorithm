import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    Ms = list(map(int, input().split()))
    lst = []
    for m in Ms:
        if m == 300:
            lst.append(1)
        elif m >= 275:
            lst.append(2)
        elif m >= 250:
            lst.append(3)
        else:
            lst.append(4)
    print(*lst)


if __name__ == '__main__':
    main()