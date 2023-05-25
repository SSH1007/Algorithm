import sys
input = sys.stdin.readline
N = int(input().rstrip())
# N의 제곱근은 무조건 N의 반보다 작다
start, end = 0, N//2
while start <= end:
    mid = (start+end)//2
    if mid**2 >= N:
        end = mid-1
    else:
        start = mid+1
print(start)