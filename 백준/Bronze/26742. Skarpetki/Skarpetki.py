import sys
input = sys.stdin.readline
BCs = input().rstrip()
B, C = 0, 0
for bc in BCs:
    if bc == 'B':
        B+=1
    else:
        C+=1
print(B//2 + C//2)