N = int(input())
lst = list(map(int, input().split()))
line = ''
for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        line += 'd'
    elif lst[i] < lst[i+1]:
        line += 'i'
    else:
        line += 'c'

lineD = line.split('d')
Dl = 0
for l in lineD:
    if len(l) > Dl:
        Dl = len(l)

lineI = line.split('i')
Il = 0
for l in lineI:
    if len(l) > Il:
        Il = len(l)

print(max(Dl,Il)+1)