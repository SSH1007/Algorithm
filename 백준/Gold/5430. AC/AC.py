import sys
input = sys.stdin.readline
from collections import deque
T = int(input().rstrip())
for _ in range(T):
    P = (input().rstrip())
    revCnt = 0
    errorFlag = False
    n = int(input().rstrip())
    lst = input().rstrip()[1:-1].split(',')
    if lst[0] == '':
        deq = deque([])
    else:
        deq = deque(list(map(int, lst)))
    for p in P:
        if p == 'R':
            revCnt+=1
        else:
            if len(deq) == 0:
                errorFlag = True
                continue
            if revCnt%2:
                deq.pop()
            else:
                deq.popleft()
    if errorFlag:
        print('error')
    else:
        if revCnt%2:
            print('['+','.join(map(str, list(reversed(deq))))+']')
        else:
            print('['+','.join(map(str, list(deq)))+']')