import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, H = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    for l in lst:
        H -= l
        cnt += 1
        if H <= 0:
            break
    if H > 0:
        print(-1)
    else:
        print(cnt)


if __name__ == '__main__':
    main()