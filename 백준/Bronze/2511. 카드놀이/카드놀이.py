import sys
input = sys.stdin.readline
alst = list(map(int, input().rstrip().split()))
blst = list(map(int, input().rstrip().split()))
aPoint, bPoint = 0, 0
winner = 'D'
for i in range(10):
    if alst[i] > blst[i]:
        aPoint += 3
        winner = 'A'
    elif alst[i] < blst[i]:
        bPoint += 3
        winner = 'B'
    else:
        aPoint += 1
        bPoint += 1
print(aPoint, bPoint)
if aPoint > bPoint:
    print('A')
elif aPoint < bPoint:
    print('B')
else:
    print(winner)