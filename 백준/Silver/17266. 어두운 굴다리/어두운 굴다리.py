import sys
input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())
Xs = [0] + list(map(int, input().rstrip().split())) + [N]
dap = 100000

def f(mid): # 해당 높이로 모든 굴다리를 비출수 있는지를 리턴
    if Xs[1]-Xs[0] > mid:       # 시작점과 첫번째 가로등 사이의 거리
        return 0
    if Xs[-1]-Xs[-2] > mid:     # 도착점과 마지막 가로등 사이의 거리
        return 0
    for i in range(1, M):
        if (Xs[i+1]-Xs[i]+1)//2 > mid:
            return 0
    return 1


# 가로등의 최소 높이를 이분탐색
s, e = 0, N
while s <= e:
    mid = (s+e)//2
    if f(mid):  # 높이가 충분하다
        dap = min(dap, mid)
        e = mid-1
    else:   # 높이가 부족하다
        s = mid+1
print(dap)