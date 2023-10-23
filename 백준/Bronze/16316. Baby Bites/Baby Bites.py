N = int(input())
lst = list(input().split())
cnt = 0
for i in range(N):
    if lst[i].isnumeric() and int(lst[i]) != i+1:
        print('something is fishy')
        break
else:
    print('makes sense')