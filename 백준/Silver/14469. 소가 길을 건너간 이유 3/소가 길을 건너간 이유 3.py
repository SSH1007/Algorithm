N = int(input())
cows = []
time = 0
for _ in range(N):
    a, t = map(int, input().split())
    cows.append((a, t))
cows.sort(key=lambda x: x[0])
for a, t in cows:
    if time <= a:
        time = a
    time += t

print(time)