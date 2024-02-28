import sys
input = sys.stdin.readline
from collections import deque
size = int(input().rstrip())
buffer = deque()
while 1:
    info = int(input().rstrip())
    if info == -1:
        break
    if info > 0 and len(buffer) < size:
        buffer.append(info)
    elif info == 0:
        buffer.popleft()
if len(buffer):
    print(*buffer)
else:
    print('empty')