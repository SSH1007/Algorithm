import heapq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    maxque = []
    minque = []
    visited = [0]*k # 최대값 힙큐와 최소값 힙큐가 같은 순번의 작업을 완수했는지를 알아보기 위한 리스트
    for i in range(k):
        DI, n = input().split()
        n = int(n)
        if DI == 'D':
            if n == 1:
                # 해당 노드가 최소값 힙에서 삭제된 노드인지 확인
                # visited[maxque[0][1]]가 1인(= 추가된) 노드가 나올때까지 모두 heappop
                while maxque and not visited[maxque[0][1]]:
                    heapq.heappop(maxque)
                if maxque:
                    visited[maxque[0][1]] = 0   # 삭제했으니 작업여부도 초기화
                    heapq.heappop(maxque)
            elif n == -1:
                # 작업 시작 전, 해당 노드가 최대값 힙에서 삭제된 노드인지 확인
                while minque and not visited[minque[0][1]]:
                    heapq.heappop(minque)
                if minque:
                    visited[minque[0][1]] = 0   # 삭제했으니 작업여부도 초기화
                    heapq.heappop(minque)
        elif DI == 'I':
            # 삽입
            heapq.heappush(maxque, (-n, i))
            heapq.heappush(minque, (n, i))
            visited[i] = 1  # 추가하면서 작업여부 갱신
    # 대상이 아닌(우선순위가 높은) 놈들을 모조리 제거
    while maxque and not visited[maxque[0][1]]:
        heapq.heappop(maxque)
    while minque and not visited[minque[0][1]]:
        heapq.heappop(minque)
    # 최대값의 경우, 넣을때 -1을 곱해줬으므로 다시 -1을 곱해서 원상복구
    if maxque and minque:
        print(-maxque[0][0], minque[0][0])
    else:
        print('EMPTY')