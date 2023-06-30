import sys
input = sys.stdin.readline
T = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
X = int(input().rstrip())
dap = []
def Euclidean(a, b):
    while b != 0:
        [a, b] = [b, a % b]
    return a
for l in lst:
    if Euclidean(l, X) == 1:
        dap.append(l)
print(sum(dap)/len(dap))