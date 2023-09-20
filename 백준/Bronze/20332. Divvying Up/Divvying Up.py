n = int(input())
ws = list(map(int, input().split()))
if (sum(ws)/3)%1:
    print('no')
else:
    print('yes')