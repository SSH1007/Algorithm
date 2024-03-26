# 부분수열은 보통 DP로 해결(시간복잡도가 O(n^2)이므로 배열 길이가 너무 크면 안 됨)
# 입력 값 크기가 크면 이분탐색으로 한다고 한다(O(log n)).
# 다만 정확한 부분 수열이 아니라 길이를 구할때 쓴다고 함
import sys
input = sys.stdin.readline
N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
dp = [0]*N
dp[0] = 1   # 수열의 최소 길이는 1이다.
for i in range(1, N):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[i], dp[j]+1)
        if not dp[i]:
            dp[i] = 1
print(max(dp))