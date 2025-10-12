import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = [0]*32
    for _ in range(N):
        b, r = map(int, input().split())
        for i in range(b, r):
            lst[i] += 1
    K = int(input())
    for i in range(32):
        if lst[i] > K:
            print(0)
            return
    print(1)


if __name__ == '__main__':
    main()