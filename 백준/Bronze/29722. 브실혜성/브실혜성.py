import math
yyyy, mm, dd = map(int, input().split('-'))
N = int(input())
yCycle = math.floor(N/360)
mCycle = math.floor(N/30 - yCycle*12)
dCycle = N % 30

dd += dCycle
if dd > 30:
    dd -= 30
    mm += 1

mm += mCycle
if mm > 12:
    mm -= 12
    yyyy += 1

yyyy += yCycle
print(str(yyyy) + '-' + str(mm).rjust(2, '0') + '-' + str(dd).rjust(2, '0'))