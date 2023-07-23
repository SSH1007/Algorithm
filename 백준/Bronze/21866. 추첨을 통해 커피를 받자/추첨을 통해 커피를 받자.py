lst = list(map(int, input().split()))
test = [100,100,200,200,300,300,400,400,500]
for n in range(9):
    if lst[n] > test[n]:
        print('hacker')
        break
else:
    if sum(lst) < 100:
        print('none')
    else:
        print('draw')