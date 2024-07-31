import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    info = list(map(int, input().split()))
    a, b = 0, 0
    s, e = 0, N-1
    tmp = 2000000000
    while s < e:
        value = abs(info[s]+info[e])
        # 딱 0이면 끝
        if value == 0:
            print(info[s], info[e])
            exit(0)

        if value < tmp:
            tmp = value
            a, b = s, e
        if info[s]+info[e] < 0:
            s += 1
        else:
            e -= 1

    print(info[a], info[b])


if __name__ == '__main__':
    main()