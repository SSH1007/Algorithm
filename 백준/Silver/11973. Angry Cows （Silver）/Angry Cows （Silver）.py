import sys
input = lambda: sys.stdin.readline().rstrip()


def check(K, lst, mid):
    point = lst[0]
    cnt = 1
    for l in lst:
        if point+(mid*2) < l:
            point = l
            cnt += 1
    # K마리 이하로 커버 가능하면 True
    return cnt <= K


def main():
    N, K = map(int, input().split())
    # 모든 K마리의 소들로 N개의 건초들을 맞출 수 있는 거리 R의 최소 값
    lst = sorted([int(input()) for _ in range(N)])
    s, e = 0, (lst[-1] - lst[0])//2
    dap = e
    while s <= e:
        mid = (s+e)//2
        if check(K, lst, mid):
            # 현재 거리로 커버가 가능하니 반경을 줄여보자
            dap = min(dap, mid)
            e = mid - 1
        else:
            s = mid + 1
    print(dap)


if __name__ == '__main__':
    main()