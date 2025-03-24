import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    y = list(map(int, input().split()))
    for _ in range(q):
        lst = list(map(int, input().split()))
        if lst[0] == 1:
            print(sum(y[lst[1]-1:lst[2]]))
            y[lst[1]-1], y[lst[2]-1] = y[lst[2]-1], y[lst[1]-1]
        else:
            print(sum(y[lst[1]-1:lst[2]])-sum(y[lst[3]-1:lst[4]]))


if __name__ == '__main__':
    main()