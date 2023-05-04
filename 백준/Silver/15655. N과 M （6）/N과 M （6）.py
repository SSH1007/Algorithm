def comb(choiceNum, choiceStart):
    if choiceNum == M:
        print(*result)
        return
    for cs in range(choiceStart, len(lst)):
        result[choiceNum] = lst[cs]
        comb(choiceNum+1, cs+1)

import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
lst = sorted(list(map(int, input().rstrip().split())))
result = [0 for _ in range(M)]
comb(0, 0)