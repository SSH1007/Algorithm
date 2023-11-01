import sys
input = sys.stdin.readline
N = int(input())
for n in range(1, N+1):
    A = input().rstrip()
    B = input().rstrip()
    A26 = [0]*26
    B26 = [0]*26
    for a in A:
        A26[ord(a)-97] += 1
    for b in B:
        B26[ord(b)-97] += 1
    dap = 0
    for i in range(26):
        dap += abs(A26[i]-B26[i])
    print('Case #%d: %d'%(n, dap))