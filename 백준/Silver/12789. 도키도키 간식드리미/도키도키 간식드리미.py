from collections import deque
N = int(input())
lst = list(map(int, input().split()))
sun = sorted(lst)
q = deque(lst)
stack = []
idx = 0
while q:
    f = q.popleft()
    if f == sun[idx]:
        idx += 1
    else:
        stack.append(f)
    while stack:
        b = stack.pop()
        if b == sun[idx]:
            idx += 1
        else:
            stack.append(b)
            break
if stack:
    print('Sad')
else:
    print('Nice')