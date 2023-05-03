def lee(n):
    # n이 2^k(k>0인 정수) 꼴인지 판별하는 함수
    while 1:
        n /= 2
        if n == 1:
            return True
        if n < 1:
            return False

import math
import sys
input = sys.stdin.readline
A, B, C = map(int, input().rstrip().split())
std = (B*B)-(4*A*C)
# 서로 다른 두 실근이 있는 경우
if std > 0:
    n = ((-1*B)+math.sqrt(B*B-(4*A*C)))/(2*A)
    m = ((-1*B)-math.sqrt(B*B-(4*A*C)))/(2*A)
    if lee(n) and lee(m):
        print('이수근')
    else:
        if int(n) == n and int(m) == m:
            print('정수근')
        else:
            print('둘다틀렸근')
else:
    print('둘다틀렸근')