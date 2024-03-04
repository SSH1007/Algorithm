import sys
input = sys.stdin.readline
N, X = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
hap = [0]*(N+1)
hap[1] = lst[0]
for i in range(2, N+1):
    hap[i] = hap[i-1]+lst[i-1]
maxhap = 0
cnt = 0
left, right = 0, X

if sum(lst) == 0:
    print('SAD')
else:
    while right < N+1:
        tmp = hap[right]-hap[left]
        if maxhap == tmp:
            cnt += 1
        elif maxhap < tmp:
            maxhap = tmp
            cnt = 1
        left += 1
        right += 1
    print(maxhap, cnt, sep='\n')