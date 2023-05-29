import sys
input = sys.stdin.readline
MOBIS = 'MOBIS'
S = input().rstrip()
for m in MOBIS:
    if m not in S:
        print('NO')
        break
else:
    print('YES')