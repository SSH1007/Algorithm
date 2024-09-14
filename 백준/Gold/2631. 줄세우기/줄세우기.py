import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left


def main():
    N = int(input())
    lst = [int(input()) for _ in range(N)]
    LIS = [lst[0]]
    for n in range(1, N):
        if lst[n] > LIS[-1]:
            LIS.append(lst[n])
        else:
            idx = bisect_left(LIS, lst[n])
            LIS[idx] = lst[n]
    print(N-len(LIS))


if __name__ == '__main__':
    main()