import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    S = list(input())
    # 1은 앞에서, 0은 뒤에서부터
    one, zero = deque(), deque()
    oCnt, zCnt = 0, 0
    for i in range(len(S)):
        if S[i] == '1':
            one.append((i, '1'))
            oCnt += 1
        else:
            zero.append((i, '0'))
            zCnt += 1
    for _ in range(oCnt//2):
        one.popleft()
    for _ in range(zCnt//2):
        zero.pop()
    dap = ['']*len(S)
    for o in one:
        dap[o[0]] = o[1]
    for z in zero:
        dap[z[0]] = z[1]
    print(''.join(dap))


if __name__ == '__main__':
    main()