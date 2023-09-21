N = int(input())
names = []
for _ in range(N):
    names.append(input())
names2 = names[::]
if sorted(names, reverse=True) == names2:
    print('DECREASING')
elif sorted(names) == names2:
    print('INCREASING')
else:
    print('NEITHER')