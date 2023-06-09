import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
# 누적합 구하기
prefixSum = [0] * (N+1)
for n in range(N):
    prefixSum[n+1] = prefixSum[n] + lst[n]

# 연속적인 K일의 온도의 합 리스트 계산
dap = []
for i in range(K, N+1):
    dap.append(prefixSum[i]-prefixSum[i-K])
print(max(dap))