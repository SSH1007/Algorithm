# ㄱ자가 ㅡ와 ㅣ의 합임을 노리고 푼 방법
mellon = int(input())
a = [int(input().split()[1]) for _ in range(6)]
i = a.index(max(a))
print((a[i-1]*a[i-2]+a[i-4]*a[i-5])*mellon)
# 가장 긴 줄 본인(a[i])과 필요없는 a[i-3]을 제외하여 계산함