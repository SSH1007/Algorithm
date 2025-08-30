import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        cb = [0]*8
        a, *lst = map(int, input().split())
        for i in range(1, 2*a, 2):
            cb[lst[i]-1] += 1
        print(max(cb))


if __name__ == '__main__':
    main()