import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, Q = map(int, input().split())
    lst = [0]*10001
    for _ in range(Q):
        a, p, b = map(int, input().split())
        if a == 1:
            lst[p] += b
        else:
            print(sum(lst[i] for i in range(p, b+1)))


if __name__ == '__main__':
    main()