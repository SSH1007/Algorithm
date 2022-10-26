A, C, E = map(int, input().split())
x, y, z = map(int, input().split())
if x>=A and y>=C and z>=E:
    print('A')
elif y>=C and z>=E:
    if x>=A/2:
        print('B')
    else:
        print('C')
elif z>=E:
    if y>=C/2:
        print('D')
    else:
        print('E')
else:
    print('E')