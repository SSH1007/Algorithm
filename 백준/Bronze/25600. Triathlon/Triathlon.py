N = int(input())
maxScore = 0
for _ in range(N):
    a, d, g = map(int, input().split())
    score = 0
    score = a*(d+g)
    if a == (d+g):
        score *= 2
    if maxScore < score:
        maxScore = score
print(maxScore)