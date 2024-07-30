import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq
# 11000번 강의실 배정과 똑같은 문제?


def main():
    N = int(input())
    info = []
    for _ in range(N):
        _, s, e = map(int, input().split())
        info.append((s, e))
    # 강의 시작 시간 순으로 정보 정렬
    info.sort()
    hq = []
    for s, e in info:
        # hq가 비어 있지 않고, hq에서 가장 이른 강의 종료 시간이
        # 주어지는 입력값(강의 시작 시간)보다 빠르다면 그대로 heappop()
        if hq and hq[0][0] <= s:
            heapq.heappop(hq)
        heapq.heappush(hq, (e, s))
    print(len(hq))


if __name__ == '__main__':
    main()