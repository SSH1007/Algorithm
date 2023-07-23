import sys
input = sys.stdin.readline
while 1:
    B, N = map(int, input().rstrip().split())
    if B == 0 and N == 0:
        break
    tmp = B**(1/N)
    at = int(tmp-1)
    bt = int(tmp+1)
    ct = int(tmp)

    a = abs(at**N - B)
    b = abs(bt**N - B)
    c = abs(ct**N - B)
    if a > b and c > b:
        print(bt)
    elif a > c and b > c:
        print(ct)
    elif b > a and c > a:
        print(at)