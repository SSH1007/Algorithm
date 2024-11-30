import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

T = int(input())
for _ in range(T):
    dic = defaultdict(int)
    M = input()
    dap = 'OK'
    for m in range(len(M)):
        dic[M[m]] += 1
        if dic[M[m]] == 4:
            dic[M[m]] = 0

        if dic[M[m]] > 0 and dic[M[m]]%3 == 0:
            if m+1 < len(M):
                if M[m] != M[m+1]:
                    dap = 'FAKE'
                    break
            else:
                dap = 'FAKE'
                break
    print(dap)