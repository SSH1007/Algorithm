import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    t, b = -float('inf'), float('inf')
    for _ in range(N):
        T, B = map(int, input().split())
        t = max(T, t)
        b = min(B, b)
    lst = [1, 2, 3, 4, 5, 6, 7]
    print(lst[(t*b)%7])


if __name__ == '__main__':
    main()