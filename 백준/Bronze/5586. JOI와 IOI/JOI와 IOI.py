import sys
input = sys.stdin.readline
S = input().rstrip()
joiCnt, ioiCnt = 0, 0
start, end = 0, 3
while end <= len(S):
    if S[start:end] == 'JOI':
        joiCnt += 1
        start += 2
        end += 2
    elif S[start:end] == 'IOI':
        ioiCnt += 1
        start += 2
        end += 2
    else:
        start += 1
        end += 1
print(joiCnt)
print(ioiCnt)