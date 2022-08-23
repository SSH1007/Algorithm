N = int(input())
lst = list(map(int,input().split()))
arr = []
for n in range(N):
    arr = arr[:lst[n]]+[(n+1)]+arr[lst[n]:]
print(*arr[::-1])