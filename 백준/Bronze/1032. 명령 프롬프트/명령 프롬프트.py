N = int(input())-1
std = list(input())
for _ in range(N):
    a = input()
    for s in range(len(std)):
        if a[s] != std[s]:
            std[s] = '?'
print(''.join(std))