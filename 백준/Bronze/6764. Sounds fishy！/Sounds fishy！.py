lst = []
for _ in range(4):
    lst.append(int(input()))
if lst[0] < lst[1] < lst[2] < lst[3] :
    print('Fish Rising')
elif lst[0] > lst[1] > lst[2] > lst[3]:
    print('Fish Diving')
elif lst[0] == lst[1] == lst[2] == lst[3]:
    print('Fish At Constant Depth')
else:
    print('No Fish')