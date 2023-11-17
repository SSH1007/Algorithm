import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    a, b = map(int, input().rstrip().split())
    S = list(input().rstrip())
    for s in range(len(S)):
        num = (a*(ord(S[s])-65)+b)%26
        S[s] = chr(num+65)
    print(''.join(S))