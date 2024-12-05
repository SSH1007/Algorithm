import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    s, e = 1, min(As)*M+1
    while s <= e:
        mid = (s+e)//2
        tmp = 0
        for a in As:
            tmp += mid//a
        if tmp >= M:
            e = mid - 1
        else:
            s = mid + 1
    print(s)


if __name__ == '__main__':
    main()