import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = [0]*31
    for _ in range(N):
        b, r = map(int, input().split())
        for i in range(b-1, r-1):
            lst[i] += 1
    K = int(input())
    for i in range(31):
        if lst[i] > K:
            print(0)
            return
    print(1)


if __name__ == '__main__':
    main()