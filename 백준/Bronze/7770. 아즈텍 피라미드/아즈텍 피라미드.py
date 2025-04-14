import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    blocks, x, y, cnt = 0, 0, 1, 0
    while 1:
        blocks += (x**2 + y**2)
        if n < blocks:
            break
        x += 1
        y += 1
        cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()