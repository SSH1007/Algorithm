import sys
input = lambda: sys.stdin.readline().rstrip()


def F(N):
    lst = []
    for n in range(1, N):
        if N % n == 0:
            lst.append(n)
    if sum(lst) == N:
        print(N, '=', ' + '.join(map(str, lst)))
    else:
        print(f'{N} is NOT perfect.')
    return


def main():
    while 1:
        N = int(input())
        if N == -1:
            break
        F(N)


if __name__ == '__main__':
    main()