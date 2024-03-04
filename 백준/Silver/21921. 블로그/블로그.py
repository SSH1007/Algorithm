import sys
input = sys.stdin.readline
N, X = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
tmp = sum(lst[:X])
max_sum = tmp
cnt = 1
if sum(lst) == 0:
    print('SAD')
else:
    for i in range(X, N):
        tmp -= lst[i-X]
        tmp += lst[i]
        if max_sum == tmp:
            cnt += 1
        elif max_sum < tmp:
            max_sum = tmp
            cnt = 1
    print(max_sum, cnt, sep='\n')