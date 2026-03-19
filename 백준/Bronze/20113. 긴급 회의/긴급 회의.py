import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    Ns = list(map(int, input().split()))
    lst = [0]*(N+1)
    for n in range(N):
        if Ns[n] != 0:
            lst[Ns[n]] += 1
    M = max(lst)
    if lst.count(M) == 1:
        print(lst.index(M))
    else:
        print('skipped')


if __name__ == '__main__':
    main()