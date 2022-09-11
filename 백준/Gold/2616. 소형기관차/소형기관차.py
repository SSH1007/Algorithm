# n:전체 객차수, m:소형기관차 제한 
n = int(input())
lst = [0]+list(map(int, input().split()))
m = int(input())

#누적합
hap = [0]*(n+1)
for i in range(n+1):
    hap[i] = lst[i]+hap[i-1]

#dp
dp = [[0]*(n+1) for _ in range(4)]
for x in range(1,4):
    for y in range(x*m, n+1):
        dp[x][y] = max(dp[x][y-1], dp[x-1][y-m]+(hap[y]-hap[y-m]))
print(dp[-1][-1])