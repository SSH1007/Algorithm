import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

def main():
    N = int(input())
    info = []
    hq = []
    for _ in range(N):
        info.append(list(map(int, input().split())))
    # 시작시간 기준으로 정렬
    info.sort(key=lambda x: x[0])
    for s, t in info:
        # 힙큐 안의 종료 시간이 가장 빠른 수업A가
        # 입력한 수업B의 시작시간과 같거나 먼저 끝난다면
        # 빼준다. (실질적으로는 A-B를 이어주는 것)
        if hq and hq[0][0] <= s:
            heapq.heappop(hq)
        heapq.heappush(hq, (t, s))
    print(len(hq))


if __name__ == '__main__':
    main()