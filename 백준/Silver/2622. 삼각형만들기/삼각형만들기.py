from math import ceil
# 가장 긴 변 길이 < 나머지 두변의 길이의 합
N = int(input())
# a, b, c. 차례대로 a가 가장 긴 변
# a는 N의 1/2보단 작아야 한다(그래야 b+c가 a보다 크기 때문).
# a는 N의 1/3과 같거나 커야 한다.
# b는 N의 1/3과 같거나 크고, a와 같거나 작아야 한다.
dap = 0
for a in range(ceil(N/3), ceil(N/2)):
    dap += (a - ceil((N-a)/2) + 1)
print(dap)