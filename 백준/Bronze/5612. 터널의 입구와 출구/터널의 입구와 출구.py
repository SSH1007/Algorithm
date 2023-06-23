import sys
input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
tunnel = [m]
for i in range(n):
    a, b = map(int, input().rstrip().split())
    tmp = tunnel[i]+a-b
    if tmp < 0:
        print(0)
        break
    tunnel.append(tmp)
else:
    print(max(tunnel))