import sys
input = sys.stdin.readline
K = int(input().rstrip())
for k in range(K):
    lst = list(map(int, input().rstrip().split()))
    score = sorted(lst[1:])
    gap = 0
    for s in range(1,len(score)):
        tmp = abs(score[s]-score[s-1])
        if tmp > gap:
            gap = tmp
    print(f'Class {k+1}')
    print(f'Max {score[-1]}, Min {score[0]}, Largest gap {gap}')