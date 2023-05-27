import sys
input = sys.stdin.readline
N = int(input().rstrip())
D, P = 0, 0
for _ in  range(N):
    if abs(D-P) >= 2:
        break
    if input().rstrip() == 'D':
        D+=1
    else:
        P+=1
print(f'{D}:{P}')