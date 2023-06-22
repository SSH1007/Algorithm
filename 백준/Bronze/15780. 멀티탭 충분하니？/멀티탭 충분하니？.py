import math
N, K = map(int, input().split())
lst = list(map(int, input().split()))
limit = sum(math.ceil(l/2) for l in lst)
print('YES' if limit>=N else 'NO')