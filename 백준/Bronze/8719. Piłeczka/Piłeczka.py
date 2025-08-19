import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    t = int(input())
    for _ in range(t):
        x, w = map(int, input().split())
        cnt = 0
        while 1:
            if x >= w:
                break
            cnt += 1
            x *= 2
        print(cnt)


if __name__ == '__main__':
    main()