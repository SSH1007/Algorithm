N = int(input())
for _ in range(N):
    P, C = map(float, input().split())
    print(P/(C+100)*100)