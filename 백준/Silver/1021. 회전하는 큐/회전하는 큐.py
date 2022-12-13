# 앞에서 뽑는 popleft가 필요하므로 deque를 쓸 것임, deque 임포트
from collections import deque
# 큐의 크기 N과 뽑아내려는 개수 M
N, M = map(int, input().split())
# 뽑아내려는 수의 위치들(M개)
nums = list(map(int, input().split()))
# ...을 deque에 넣음
deq = deque(list(range(1,N+1)))
# 오른쪽으로 이동, 혹은 왼쪽으로 이동한 총 횟수
dap = 0
# 뽑아내려는 숫자 목록에서 반복문 돌림
for i in nums:
    # 1번째 연산 : 첫번째 원소가 뽑아내려는 원소와 같다면, 그 수를 뽑아낸다.
    if deq[0]==i:
        deq.popleft()
    # 아니라면, 
    else:
        # 0~i의 거리가 i~len(deq)의 거리보다 작다면
        if deq.index(i) < len(deq)-deq.index(i):
            # 첫번째 원소가 뽑아내려는 원소와 같아질 때까지
            while 1:
                # 앞에서 뽑아서 뒤로 보낸다.
                a = deq.popleft()
                deq.append(a)
                # 연산 수행 횟수는 더해주고
                dap+=1
                # 같아지면 브레이크
                if deq[0] == i:
                    break
        # 0~i의 거리가 i~len(deq)의 거리보다 크거나 같다면,
        else:
            # 첫번째 원소가 뽑아내려는 원소와 같아질 때까지
            while 1:
                # 뒤에서 뽑아서 앞으로 보낸다.
                a = deq.pop()
                deq.appendleft(a)
                # 연산 수행 횟수는 더해주고
                dap+=1
                # 같아지면 브레이크
                if deq[0] == i:
                    break
        # 첫번째 원소가 뽑아내려는 원소와 같아졌으므로 1번째 연산 수행
        deq.popleft()
# 연산 총 수행 횟수를 출력
print(dap)