import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    stt = input().rstrip()
    obj = input().rstrip()
    W = abs(stt.count('W')-obj.count('W'))
    diff = 0
    for n in range(N):
        if stt[n] != obj[n]:
            diff += 1
    print(W+(diff-W)//2)