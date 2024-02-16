import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    a, b, c = map(int, input().rstrip().split())
    aa = (b+c)**2+a**2
    bb = (a+c)**2+b**2
    cc = (a+b)**2+c**2
    print(min(aa, bb, cc))
