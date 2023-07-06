import sys
input = sys.stdin.readline

S1, S2 = map(int, input().rstrip().split())
sample = True
system = True
for _ in range(S1):
    s, m = map(int, input().rstrip().split())
    if s!=m:
        sample = False
        break
for _ in range(S2):
    s, m = map(int, input().rstrip().split())
    if s!=m:
        system = False
        break
if sample and system:
    print('Accepted')
elif sample and not system:
    print('Why Wrong!!!')
elif not sample and system:
    print('Wrong Answer')