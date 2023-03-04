apple1 = int(input())
apple2 = int(input())
apple3 = int(input())
banana1 = int(input())
banana2 = int(input())
banana3 = int(input())
if apple1*3+apple2*2+apple3 > banana1*3+banana2*2+banana3:
    print('A')
elif apple1*3+apple2*2+apple3 < banana1*3+banana2*2+banana3:
    print('B')
else:
    print('T')