a, b = map(int, input().split())
c, d = map(int, input().split())
fence = [0 for _ in range(100)]
for i in range(a, b):
    fence[i] = 1
for i in range(c, d):
    fence[i] = 1
print(fence.count(1))