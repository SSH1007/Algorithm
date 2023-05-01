def perm(lst, leng, stack, used):
    if len(stack) == leng:
        print(*stack)
        return
    for i in range(len(lst)):
        if not used[i]:
            stack.append(lst[i])
            used[i] = 1
            perm(lst, leng, stack, used)
            used[i] = 0
            stack.pop()

import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
lst = sorted(list(map(int, input().rstrip().split())))
used = [0 for _ in range(N)]
perm(lst, M, [], used)