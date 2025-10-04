import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    lst = [0]*(N+1)
    for n in range(1, N+1):
        A = int(input())
        lst[n] = A
    for m in range(1, M+1):
        for n in range(1, N):
            if lst[n]%m > lst[n+1]%m:
                lst[n], lst[n+1] = lst[n+1], lst[n]
    for n in range(1, N+1):
        print(lst[n])


if __name__ == '__main__':
    main()