import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq


def main():
    N, K = map(int, input().split())
    kids = list(map(int, input().split()))

    # 예제)
    # 1, 3, 5, 6, 10의 차의 집합 hq
    # hq = [2, 2, 1, 4]
    # k=5: 1, 3, 5, 6, 10 => 0
    # k=4: 1, 3, 5,6, 10 => 1
    # k=3: 1,3, 5,6, 10 => 3
    # k=2: 1,3,5,6, 10 => 5
    # k=1: 1,3,5,6,10 => 9
    # ∴ 가장 큰 값을 계속 빼주면 된다

    # heapq를 사용. 작은 값부터 빼는 최소힙이므로
    # -1을 곱해서 절대값이 큰놈부터 나오게 한다.
    hq = []
    for i in range(1, N):
        hq.append(-1 * (kids[i]-kids[i-1]))
    heapq.heapify(hq)
    for _ in range(K-1):
        heapq.heappop(hq)
    print(sum(hq)*-1)


if __name__ == '__main__':
    main()