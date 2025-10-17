import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    lst = [0]*(M+1)
    X = list(map(int, input().split()))
    for n in range(N):
        lst[X[n]] += 1
    print(max(lst))


if __name__ == '__main__':
    main()