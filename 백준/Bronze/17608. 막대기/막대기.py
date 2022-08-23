import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    h = int(input())
    stack.append(h)
cnt = 1
front = stack.pop()
while stack:
    current = stack.pop()
    if current > front:
        front = current
        cnt+=1
print(cnt)