import math
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(math.ceil(a/b))