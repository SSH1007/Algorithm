import sys
input = sys.stdin.readline
N = int(input().rstrip())
start, end = 0, N//2
while start <= end:
    mid = (start+end)//2
    if mid**2 > N:
        end = mid-1
    else:
        start = mid+1
print(end)