import sys
input = sys.stdin.readline
A, B, C = map(int, input().rstrip().split())
day = 0
coin = 0
while coin < C:
    day += 1
    coin += A
    if day % 7 == 0:
        coin += B
print(day)