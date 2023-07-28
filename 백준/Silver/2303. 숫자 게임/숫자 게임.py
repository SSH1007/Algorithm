import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = []
for n in range(N):
    tmp = list(map(int, input().rstrip().split()))
    std = 0
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                std = max(std, int(str(tmp[i]+tmp[j]+tmp[k])[-1]))
    lst.append((n+1, std))
lst.sort(key=lambda x: (-x[1], -x[0]))
print(lst[0][0])