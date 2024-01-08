import sys
input = sys.stdin.readline
while 1:
    N, M = map(int, input().rstrip().split())
    if N == M == 0:
        break
    sk, sy = set(), set()
    for _ in range(N):
        n = int(input().rstrip())
        sk.add(n)
    for _ in range(M):
        m = int(input().rstrip())
        sy.add(m)
    hap = sk|sy
    print(N+M-len(hap))