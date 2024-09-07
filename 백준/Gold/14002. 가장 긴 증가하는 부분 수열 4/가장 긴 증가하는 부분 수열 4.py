# 14002 : 가장 긴 증가하는 부분 수열 4 - bisect
import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left


def main():
    N = int(input())
    As = list(map(int, input().split()))
    # 최장 증가 부분 수열
    LIS = []
    # LIS 각 원소의 갱신 시 해당 원소가 위치했던 인덱스 목록
    LIS_idx = []
    # LIS 각 원소의 갱신 시 해당 원소가 위치했던 인덱스 바로 앞의 인덱스 목록(역추적용)
    LIS_prev_idx = [-1]*N

    for n in range(N):
        idx = bisect_left(LIS, As[n])
        if idx >= len(LIS):
            LIS.append(As[n])
        else:
            LIS[idx] = As[n]

        if idx > 0:
            LIS_prev_idx[n] = LIS_idx[idx-1]
        if idx >= len(LIS_idx):
            LIS_idx.append(n)
        else:
            LIS_idx[idx] = n

    restore = []
    idx = LIS_idx[-1]
    while idx != -1:
        restore.append(As[idx])
        idx = LIS_prev_idx[idx]
    print(len(restore))
    print(*restore[::-1])


if __name__ == '__main__':
    main()