from collections import deque
T = int(input())
for _ in range(T):
    N = int(input())
    cards = list(input().split())[::-1]
    q = deque()
    while cards:
        if not q:
            q.append(cards.pop())
        else:
            al = cards.pop()
            if q[0] >= al:
                q.appendleft(al)
            elif q[-1] <= al:
                q.append(al)
            else:
                q.append(al)
    print(*q,sep='')