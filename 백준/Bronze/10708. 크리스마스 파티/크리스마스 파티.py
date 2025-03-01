import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    M = int(input())
    friend = [0]*N
    target = list(map(int, input().split()))
    for m in range(M):
        tmp, miss = 0, 0
        lst = list(map(int, input().split()))
        for n in range(N):
            if lst[n] == target[m]:
                friend[n] += 1
            else:
                miss += 1
        friend[target[m]-1] += miss
    print(*friend, sep = '\n')


if __name__ == '__main__':
    main()