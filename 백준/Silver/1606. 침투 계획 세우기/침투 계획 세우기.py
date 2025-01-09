import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    r, c = map(int, input().split())
    tmp = 1
    for i in range(r+c):
        tmp += 6*i
    print(tmp+c)


if __name__ == '__main__':
    main()