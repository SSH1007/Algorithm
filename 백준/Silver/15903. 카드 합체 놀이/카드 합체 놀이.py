# 목표 : m번의 합체를 모두 끝낸 뒤, 모든 카드의 수를 더한 값이 최소값이 되어야 한다.
import sys
input = sys.stdin.readline
import heapq
# 카드의 개수 n(<=1000), 합체 수 m(<=15000)
# 기존 풀이대로 m번마다 n개를 정렬시키는 것은 최대 15,000,000번이기 때문에
# m번마다 정렬보다는 우선순위 큐가 더 빠르다.
n, m = map(int, input().rstrip().split())
# 맨 처음 카드의 상태
As = list(map(int, input().rstrip().split()))
# 리스트를 우선순위 큐로 변환
heapq.heapify(As)

for _ in range(m):
    a, b = heapq.heappop(As), heapq.heappop(As)
    c = a+b
    heapq.heappush(As, c)
    heapq.heappush(As, c)
print(sum(As))