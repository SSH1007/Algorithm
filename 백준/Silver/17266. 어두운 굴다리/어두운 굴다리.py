import sys
input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())
X = list(map(int, input().rstrip().split()))
diff = []
for i in range(1, M):
    diff.append(X[i]-X[i-1])
frontD = X[0]-0
backD = N-X[-1]
diff.extend((frontD*2, backD*2))
print((max(diff)+1)//2)