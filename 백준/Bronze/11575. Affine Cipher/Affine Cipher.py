T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    S = input()
    for s in S:
        print(chr((a*(ord(s)-65)+b) % 26 + 65), end='')
    print()