import sys
input = sys.stdin.readline
M, S, G = map(int, input().rstrip().split())
A, B = map(float, input().rstrip().split())
L, R = map(int, input().rstrip().split())
# LGMA
# RSMB
# 가만히 있으면 1명당 M/S 초가 걸린다.
stand = M/S + R/B
# 걸어올라가면 1명당 M/G초가 걸린다.
walk = M/G + L/A
if stand < walk:
    print('latmask')
else:
    print('friskus')